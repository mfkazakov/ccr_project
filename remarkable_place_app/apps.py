from django.apps import AppConfig
from constance import config


class RemarkablePlaceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'remarkable_place_app'

    def ready(self):
        """После того как приложение ready запуск периодической задачи на получение погоды"""
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

