import os
import json
import time
import redis
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def fib(x):
    """Recursively calculate the fibonacci value given an index.

    """
    if x <= 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2) 


def cached_fib(x, r):
    """Calculate the fibonacci value for a given index using cached values
    when possible.

    """
    if x <= 1:
        return 1
    else:
        prev1 = fib(x - 1) if r.get(x - 1) == None else r.get(x - 1)
        prev2 = fib(x - 2) if r.get(x - 2) == None else r.get(x - 2)
        return int(prev1) + int(prev2)


def redis_connect():
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    r = redis.Redis(host=host, port=port, db=0)
    return r


def response(message):
    res = Response(json.dumps(message))
    res.status_code = 200
    res.content_type = "application/json"
    return res


@app.route("/")
@cross_origin()
def home():
    return response("OK")


@app.route("/api/fib", methods=["POST"])
@cross_origin()
def calculate():
    """Calculate the fibonacci sequence value every time. Store values in
    Redis cache with execution time [ms].

    """
    data = json.loads(request.data)
    x = int(data['input'])
    start = time.time()
    y = fib(x)
    duration = time.time() - start

    r = redis_connect()
    r.set(x, y)
    return response({
        'value': y, 'duration': duration * 10**3
    })


@app.route("/api/cached_fib", methods=["POST"])
@cross_origin()
def cached_calculate():
    """Attempt to use cached values to compute the fibonacci value.
    Store in cache with execution time.

    """
    r = redis_connect()
    data = json.loads(request.data)
    x = int(data['input'])
    start = time.time()
    y = cached_fib(x, r)
    duration = time.time() - start
    return response({
        'value': y, 'duration': duration * 10**3
    })


@app.route("/api/cache", methods=["GET"])
@cross_origin()
def get_cache():
    """Return the contents of the cache.

    """
    r = redis_connect()
    cache = {}
    for k in r.keys():
        cache[json.loads(k)] = json.loads(r.get(k))
    return response(cache)