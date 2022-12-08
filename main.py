from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os
import spacy
from celery import Celery
from config import Config
from celery.result import AsyncResult

app = Flask(__name__)
app.config.from_object(Config)

# CELERY_TASK_LIST = [
#     'tasks'
# ]

def make_celery():
    celery = Celery(
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        #include=CELERY_TASK_LIST

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
celery = make_celery()

@celery.task(name='web.getAnswer')
def getResult(f_s, s_s):
    nlp = spacy.load("ru_core_news_lg")
    f_s = nlp(f_s)
    s_s = nlp(s_s)
    return f_s.similarity(s_s)
    



@app.route('/<string:correct>/<string:user_answer>')
async def ind(correct, user_answer):
    ans = getResult.delay(user_answer, correct)
    return jsonify({"A": ans.get()})
    

    
@app.route('/')
def hello():
    return jsonify({"Ans": "Test"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), threaded=True)
