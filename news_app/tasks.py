from celery import shared_task
from .models import News
from django.utils.timezone import localdate
from constance import config


@shared_task()
def send_main_today_news():
    """Отправка почты"""
    title = config.TITLE if config.TITLE else ''
    emails = config.EMAILS.replace(' ', '').split(',') if config.EMAILS else ''
    body = config.BODY + '\n' if config.BODY else ''

    news = News.objects.filter(publication_date=str(localdate())).all()

    if news:
        for news_ in news:
            body += news_.title
            body += '\n'
    else:
        body += 'Новостей за сегодня нет\n'

    messages = []
    for email in emails:
        messages.append((title, body, 'from@example.com',email))
        print(f'''Send email to {email}
        title - {title}
        body - {body}''')

    """
    Далее отправка через send_mass_mail() из messages, настройки в settings не заполнял.
    Настройки:
    EMAIL_USE_TLS = 
    EMAIL_USE_SSL =
    EMAIL_HOST = 
    EMAIL_PORT = 
    EMAIL_HOST_USER = 
    EMAIL_HOST_PASSWORD = 
    
    """

