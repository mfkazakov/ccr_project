#!/bin/bash

sleep 5

python manage.py flush --no-input

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
python -m celery -A ccr_project worker
celery -A ccr_project beat
exec "$@"

