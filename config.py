class Config:
    CELERY_BROKER_URL = 'amqp://guest:0.0.0.0:5672//'
    CELERY_RESULT_BACKEND = 'rpc://'