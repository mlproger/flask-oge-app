import text_sum
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os
from celery import Celery
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CELERY_TASK_LIST = [
    'main.tasks'
]

def make_celery():
    celery = Celery(
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        include=CELERY_TASK_LIST

    )

    celery.conf.task_routes = {
        'web.*': {'queue': 'web'}
    }

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery



@app.route('/<string:correct>/<string:user_answer>')
async def ind(correct, user_answer):
    ans = text_sum.getResult(user_answer, correct)
    return jsonify({"A": ans})
    

    
@app.route('/')
def hello():
    return jsonify({"Ans": "Test"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), threaded=True)
