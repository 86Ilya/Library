#!/bin/bash

python /app/manage.py makemigrations 
python /app/manage.py collectstatic --noinput
# UGLY HACK for waiting databases
sleep 3
python /app/manage.py migrate --database=default
python /app/manage.py migrate --database=replica
python /app/manage.py populate
echo "launching uwsgi"
uwsgi --ini /app/docker/web_service/uwsgi.ini 
