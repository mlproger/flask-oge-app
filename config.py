class Config:
    CELERY_BROKER_URL = 'amqp://'
    CELERY_RESULT_BACKEND = 'rpc://'