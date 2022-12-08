web: gunicorn main:app
celery: celery -A main.celery worker --ool=solo -Q web