from flask import Flask, render_template, request, make_response, g
from redis import Redis
import urllib.request
import os
import socket
import random
import json as JSON

hostname = socket.gethostname()

app = Flask(__name__)

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis
pushes = 0
@app.route("/", methods=['POST','GET'])
def hello():
    global pushes
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]
    url = "http://localhost:5001/restos"
    res = urllib.request.urlopen(url).read().decode("utf-8")
    if res == "":
        return "Error get restos"
    if request.method == 'POST':
        redis = get_redis()
        if not redis: 
            return "problem" 
        data = JSON.dumps({'voter_id': voter_id,'resto_name':request.form["resto_name"], 'name': request.form["name"], 'date': request.form["date"], 'time':request.form["time"], 'people': request.form["people"]})
        pushes = redis.rpush('bookings', data)
    resp = make_response(render_template(
        'index.html',
        restaurants = JSON.loads(res),
        hostname=hostname,
        len = pushes,
        reservations=[["aaa", "22.5.1990", "20:20", "3"], ["bbb", "25,02,1990", "18:00", "44"]],
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
