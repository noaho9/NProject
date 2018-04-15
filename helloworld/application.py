#!flask/bin/python
#added this code from gist 1 slack 15-04-18
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))

import json
from flask import Flask, Response, request
from helloworld.flaskrun import flaskrun
#add this for th
import requests


application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello Get World'}), mimetype='application/json', status=200)
    
  #adding a route for getting the IP address
@application.route('/get_ip', methods=['GET'])

#added this function for getting the IP address  
def get_ip():
    #print(get_ip_meta())
    return Response(json.dumps(get_ip_meta()), mimetype='application/json', status=200)
    
    

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello Post World in cloud 9'}), mimetype='application/json', status=200)


def get_ip_meta():
    user_ip = str(request.environ['REMOTE_ADDR'])
    service_url = 'http://ipinfo.io/{}'.format(user_ip) 
    return requests.get(service_url).json()
    
    
if __name__ == '__main__':
    flaskrun(application)

