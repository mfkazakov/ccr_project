import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ccr_project.settings")

app = Celery("ccr_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


#python -m celery -A ccr_project worker -l INFO
#python -m celery -A ccr_project beat -l INFO
#python -m celery -A ccr_project flower --address=127.0.0.1 --port=5566

