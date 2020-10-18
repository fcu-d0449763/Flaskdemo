from flask import Flask, jsonify
from flask import request

from flask.views import MethodView
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "OK"

@app.route('/req', methods=['GET','POST'])
def req():
    if request.method == 'GET':
        return "Request Header:\n"+str(request.headers)+str(request.args)
    else:
        return request.json




    


class API_Test(MethodView):
    def get(self):
        return jsonify(message='I am GET')

    def post(self):
        return jsonify(message='I am POST')
        

    def put(self):
        return jsonify(message='I am PUT')

    def delete(self):
        return jsonify(message='I am DELETE')




app.add_url_rule('/test_api/', view_func=API_Test.as_view('test_api'))



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)