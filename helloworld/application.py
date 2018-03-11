#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello Get World'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello Post World'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(application)
