#!/usr/bin/env bash

python3 manage.py collectstatic && \
python3 manage.py makemigrations && \
python3 manage.py migrate && \
uwsgi --ini /app/mysite/uwsgi.ini &
npm --prefix /app/mysite/frontend run dev &
nginx -c /etc/nginx/nginx.conf
#python3 manage.py runserver --noreload 0.0.0.0:8000
