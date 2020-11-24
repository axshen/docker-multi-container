import os
import json
import time
from flask import Flask, Response
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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
    pass


@app.route("/api/fib", methods=["GET"])
@cross_origin()
def calculate():
    pass