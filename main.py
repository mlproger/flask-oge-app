import text_sum
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
api = Api(app)

limiter = Limiter(
    app,
    default_limits=["200 per day", "50 per hour"],
    key_func=get_remote_address,
    #storage_uri="https://localhost:5000",
)



@app.route('/<string:correct>/<string:user_answer>')
@limiter.limit("2/seconds")
async def ind(correct, user_answer):
    return jsonify({"A": text_sum.getResult(user_answer, correct)})
    
    
    
@app.route('/test')
def hello():
    return jsonify({"Ans": "Test"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), threaded=True)
