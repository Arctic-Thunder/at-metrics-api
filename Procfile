release: python manage.py makemigrations --noinput; python manage.py migrate --noinput
web: gunicorn metrics-api.wsgi
