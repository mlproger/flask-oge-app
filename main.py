from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os
import text_sum
from celery import Celery
import spacy

def getResult(f_s, s_s):
    nlp = spacy.load("ru_core_news_lg")
    f_s = nlp(f_s)
    s_s = nlp(s_s)
    return f_s.similarity(s_s)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery



app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL="/http://localhost:5000/",
    CELERY_RESULT_BACKEND="/http://localhost:5000/",
)
api = Api(app)
celery = make_celery(app)

@celery.task()
def rec(correct, user_answer):
    return text_sum.getResult(user_answer, correct)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/<string:correct>/<string:user_answer>')
def ind(correct, user_answer):
    results = rec(correct, user_answer)
    return jsonify(results)
    
    
     

@app.route('/test')
def hello():
    return jsonify({"Ans": "Test"})




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), threaded=True)
