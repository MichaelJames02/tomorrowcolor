web: gunicorn -c gunicorn_config.py tomorrowcolor.wsgi
worker: celery worker --app=tomorrowcolor.taskapp --loglevel=info
