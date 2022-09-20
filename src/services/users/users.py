from crypt import methods
from queue import Empty
from urllib import response
from flask import Blueprint, request, jsonify, Response
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from werkzeug.exceptions import BadRequest
import certifi

users = Blueprint("users", __name__)
uri = "mongodb+srv://ivanwekis:MmongodbB@cluster0.srdnijs.mongodb.net/test"
ca = certifi.where()
client = MongoClient(uri, tlsCAFile=ca)
db = client["nasdaq-users"]


@users.route("/new_user", methods=["POST"])
def new_user():
    try:
        username = request.json["username"]
        email = request.json["email"]
        password = request.json["password"]
        rpassword = request.json["rpassword"]
    except KeyError as error:
        return jsonify({"response":"The data isn`t correct", "error": str(error)})

    if password == rpassword:
        query = {"username": username}
        query2 = {"email": email}
        if db.users.find_one(query) is None:
            if db.users.find_one(query2) is None:
                hashed_password = generate_password_hash(password)
                new_user = {
                    "username": username,
                    "email": email,
                    "password": hashed_password,
                }
                db.users.insert_one(new_user)
                return jsonify({"response":"The new user have been added"})
            else:
                return jsonify({"response": "Alredy exists an account with that email"})

        else:
            return jsonify({"response": "Alredy exists that username"})

    else:
        return jsonify({"response": "Please check the passwords"})

@users.app_errorhandler(BadRequest)
def error_handler():
    return jsonify({"response":"The data isn`t correct"})