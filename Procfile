web: gunicorn main:app
celery: celery -A main.celery worker --pool=solo -Q web