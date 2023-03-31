from constance.signals import config_updated
from django.dispatch import receiver
from constance import config
import zoneinfo
from django.conf import settings


@receiver(config_updated)
def constance_updated(sender, key, old_value, new_value, **kwargs):
    """Вызывается при изменении времени рассылки почты"""
    if key == 'TIME':
        from django_celery_beat.models import PeriodicTask, CrontabSchedule
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=config.TIME.minute,
            hour=config.TIME.hour,
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
            timezone=zoneinfo.ZoneInfo(settings.CELERY_TIMEZONE)
        )

        PeriodicTask.objects.update_or_create(name='send_mail', defaults={
                'crontab': schedule,
                'task': 'news_app.tasks.send_main_today_news'
            })

