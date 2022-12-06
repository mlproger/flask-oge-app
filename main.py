import text_sum
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os


app = Flask(__name__)
api = Api(app)



@app.route('/<string:correct>/<string:user_answer>')
async def ind(correct, user_answer):
    return jsonify({"A": text_sum.getResult(user_answer, correct)})
    
@app.route('/')
def hi():
    return jsonify({"Ans": "HI"})   
    
@app.route('/test')
def hello():
    return jsonify({"Ans": "Test"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), threaded=True)
