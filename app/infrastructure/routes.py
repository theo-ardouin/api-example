from flask import Flask, request, jsonify
from os import environ
from sqlite3 import connect
from typing import Any
from dataclasses import asdict
from app.adapters.user.factory import create
from app.usecases import CreateUser, GetUser, GetEmails
from app.adapters import JsonUser, RequestsCat, SqlUser, MemoryUser
from app.entities import InvalidEmail, UserNotFound, UserAlreadyExists

app = Flask(__name__)
cat = RequestsCat(environ["CAT_API_KEY"])


def database() -> Any:
    return create(SqlUser, connect("test.db"))
    # return create(JsonUser, open("test.json", "r+"))
    # return create(MemoryUser)


@app.route("/users", methods=["POST"])
def create_user() -> Any:
    try:
        with database() as db:
            return jsonify(
                asdict(CreateUser(db, cat).execute(request.get_json()["email"]))
            ), 201
    except KeyError:
        return jsonify({"message": "missing email"}), 400
    except InvalidEmail:
        return jsonify({"message": "invalid email"}), 400
    except UserAlreadyExists:
        return jsonify({"message": "user already exists"}), 409
    except:
        return jsonify({"message": "unexpected error"}), 500


@app.route("/users", methods=["GET"])
def get_users() -> Any:
    try:
        with database() as db:
            return jsonify(GetEmails(db).execute())
    except:
        return jsonify({"message": "unexpected error"}), 500


@app.route("/users/<email>", methods=["GET"])
def get_user(email: str) -> Any:
    try:
        with database() as db:
            return jsonify(asdict(GetUser(db).execute(email)))
    except InvalidEmail:
        return jsonify({"message": "invalid email"}), 400
    except UserNotFound:
        return jsonify({"message": "user not found"}), 404
    except:
        return jsonify({"message": "unexpected error"}), 500
