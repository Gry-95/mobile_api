#!/bin/bash

./wait-for-it.sh db:5432 --timeout=30

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/workers.json
python manage.py loaddata fixtures/shops.json
# python manage.py test

exec gunicorn conf.wsgi:application --bind 0:8000
