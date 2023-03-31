from django.apps import AppConfig
from constance import config
import zoneinfo
from django.conf import settings


class NewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_app'

    def ready(self):
        """После того как приложение ready запуск периодической задачи на отправку почты"""
        from django_celery_beat.models import PeriodicTask, CrontabSchedule

        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=config.TIME.minute,
            hour=config.TIME.hour,
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
            timezone=zoneinfo.ZoneInfo(settings.CELERY_TIMEZONE)
            )

        PeriodicTask.objects.update_or_create(
            name='send_mail',
            defaults={
                'crontab': schedule,
                'task': 'news_app.tasks.send_main_today_news'
                }
            )
