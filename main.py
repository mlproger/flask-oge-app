from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os
import text_sum


class CRUDClass(Resource):
    def get(self, correct, user_answer):
        return jsonify({text_sum.getResult(user_answer, correct)})

app = Flask(__name__)
api = Api(app)
api.add_resource(CRUDClass, "/<string:correct>/<string:user_answer>")


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
