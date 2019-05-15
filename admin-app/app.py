from flask import Flask, render_template, request, make_response, g
import os
import socket
import random
import urllib.request
import json as JSON
from redis import *

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()

app = Flask(__name__)
addr = "localhost"

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis

@app.route("/", methods=['POST','GET'])
def hello():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None
    
    redis = get_redis()
    if not redis: 
        return "problem" 
    if request.method == 'POST':
        return "ceva"
    req = []
    while redis.llen('bookings') != 0:
        req += [JSON.loads(redis.lpop('bookings'))]
    resp = make_response(render_template(
        'index.html',
        hostname=hostname,
        requests=req,
        tables={3: [3, 1, 2], 2: [9, 10, 11, 12], 1: [6,7, 8, 5, 4]},
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp

@app.route("/restos")
def get_restos():
    url = "http://manager-app:5002/get_restos"
    res = urllib.request.urlopen(url).read().decode("utf-8")
    #restos = JSON.loads(res)
    #r_name = []
    #for r in restos:
     #   r_name += [r["name"]]
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)
