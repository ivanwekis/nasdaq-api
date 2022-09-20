from crypt import methods
from urllib import request
from flask import Blueprint, jsonify, request, Response
from pymongo import MongoClient
from werkzeug.security import check_password_hash
import certifi
from bson import json_util

querys = Blueprint("querys",__name__)
uri = "mongodb+srv://ivanwekis:MmongodbB@cluster0.srdnijs.mongodb.net/test"
ca = certifi.where()
client = MongoClient(uri, tlsCAFile=ca)
dbnasdaq = client["nasdaq"]
dbusers = client["nasdaq-users"]

@querys.route("/stocks/<stock>", methods=["POST", "GET"])
def info_stock(stock):
    if request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]
        user =  dbusers.users.find_one({'username': username})
        print(user)
        if check_password_hash(user["password"],password):
            stock_data =  dbnasdaq.get_collection(stock)
            data = json_util.dumps(stock_data)
            return Response(data, mimetype="application/json")
            
        else:
            return jsonify({"response": "The username or password are invalid "})

    if request.method == "GET":
        return jsonify({"response": "This method not is allowed, only POST with user credentials"})
    else:
        return jsonify({"response": "This method not is allowed, only POST with user credentials"})


@querys.errorhandler(404)
def not_found():
    return jsonify({"response":"Invalid route"})