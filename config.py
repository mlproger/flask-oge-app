class Config:
    CELERY_BROKER_URL = 'amqp://0.0.0.0:5672//'
    CELERY_RESULT_BACKEND = 'rpc://'