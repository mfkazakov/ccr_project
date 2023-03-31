from constance.signals import config_updated
from django.dispatch import receiver
from constance import config
from datetime import timedelta


@receiver(config_updated)
def constance_updated(sender, key, old_value, new_value, **kwargs):
    """Вызывается при изменении частоты загрузке погоды"""
    if key == 'TIME_INTERVAL_WEATHER':
        if int(config.TIME_INTERVAL_WEATHER.total_seconds()) < 60:  # не чаще раза в минуту доступ к погоде
            config.TIME_INTERVAL_WEATHER = timedelta(minutes=1)

        from django_celery_beat.models import PeriodicTask, IntervalSchedule

        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=int(config.TIME_INTERVAL_WEATHER.total_seconds())/60,
            period=IntervalSchedule.MINUTES
        )

        PeriodicTask.objects.update_or_create(
            name='get_weather', defaults=
            {
                'interval': schedule,
                'task': 'remarkable_place_app.tasks.get_weather'
            })

