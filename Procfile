web: gunicorn tomorrowcolor.wsgi
worker: celery -A tasks worker --app=tomorrowcolor.taskapp --loglevel=info
