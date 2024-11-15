from app import app, config
from app.util import password_util as password_util, database_util as database_util
from flask import request, jsonify
import re


def is_username_valid(username):
    return re.fullmatch(r"\s{3,16}", username)


def is_password_valid(password):
    return re.fullmatch(r".{5,20}", password)


@app.route("/api/v1/signup", methods=["POST"])
def signup():
    content = request.json
    if not content:
        return jsonify({"success": False, "error": "Did not specify json body"}), 400
    elif "username" not in content:
        return jsonify({"success": False, "error": "Username field not present"}), 403
    elif "password" not in content:
        return jsonify({"success": False, "error": "Password field not present"}), 403

    username, password = content["username"], content["password"]

    if not is_username_valid(username):
        return jsonify({"success": False, "error": "Username is not valid"}), 403
    elif not is_password_valid(password):
        return jsonify({"success": False, "error": "Password is not valid"}), 403
    elif database_util.does_user_exist(username):
        return jsonify({"success": False, "error": "Username already exists"}), 403

    hashed_password = password_util.hash_password(password)
    database_util.add_user(username, hashed_password)

    return jsonify({"success": True}), 200


@app.route("/api/v1/login", methods=["POST"])
def login():
    content = request.json
    if not content:
        return jsonify({"success": False, "error": "Did not specify json body"}), 400
    elif "username" not in content:
        return jsonify({"success": False, "error": "Username field not present"}), 403
    elif "password" not in content:
        return jsonify({"success": False, "error": "Password field not present"}), 403

    username, password = content["username"], password_util.hash_password(content["password"])

    if database_util.does_cred_match(username, password):
        session_id = config.session_manager.create_session(username)
        return jsonify({"success": True, "session_id": session_id}), 200
    else:
        return jsonify({"success": False, "error": "Username and Password do not match"}), 401
