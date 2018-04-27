web: gunicorn config.wsgi:application
worker: celery -A tasks worker --app=tomorrowcolor.taskapp --loglevel=info
