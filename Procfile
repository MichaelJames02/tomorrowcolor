web: gunicorn -c gunicorn_config.py tomorrowcolor.wsgi
worker: celery -A tasks worker --app=tomorrowcolor.taskapp --loglevel=info
