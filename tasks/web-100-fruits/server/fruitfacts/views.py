from flask import render_template, request, abort, jsonify
from fruitfacts import app
from fruitfacts.db import db


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get():
    r_filter = request.get_json()
    res = [i for i in db["fruits"].find(r_filter)]
    for i in res:
        del i["_id"]
    return jsonify(res)
