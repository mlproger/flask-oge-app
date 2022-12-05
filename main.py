from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import text_sum


# class CRUDClass(Resource):
#     def get(self, correct, user_answer):
#         return text_sum.getResult(user_answer, correct)

app = Flask(__name__)
api = Api(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)
#api.add_resource(CRUDClass, "/<string:correct>/<string:user_answer>")


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/<string:correct>/<string:user_answer>')
@limiter.limit("1/seconds")
def rec(correct, user_answer):
    ans = text_sum.getResult(user_answer, correct)
    return jsonify({"ans": ans})

@app.route('/test')
def hello():
    return jsonify({"Ans": "Test"})




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), threaded=True)
