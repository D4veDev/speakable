#!/bin/bash</strong>
source /venv/bin/activate
cd /app/speakable

echo "----- Collect static files ------ " 
python manage.py collectstatic --noinput

echo "-----------Apply migration--------- "
python manage.py makemigrations 
python manage.py migrate

echo "-----------Run gunicorn--------- "
gunicorn -b :5000 myapp.wsgi:application
