from app import app, config
from flask import request, jsonify
from app.util import database_util as database_util


@app.route("/api/v1/leaderboard", methods=["GET"])
def leaderboard():
    return database_util.get_top10_leaderboard()


@app.route("/api/v1/update_score", methods=["POST"])
def update_score():
    content = request.json
    if not content:
        return jsonify({"success": False, "error": "Did not specify json body"}), 400
    elif "session_id" not in content:
        return jsonify({"success": False, "error": "session_id id field not present"}), 403
    elif "score" not in content:
        return jsonify({"success": False, "error": "score field not present"}), 403
    elif not isinstance(content["score"], int):
        return jsonify({"success": False, "error": "score field is not an integer"}), 403

    session_id, score = content["session_id"], content["score"]
    session = config.session_manager.get_session(session_id)

    if not session:
        return jsonify({"success": False, "error": "There are no active sessions associated with session_id"}), 403

    username = session.username
    current_score = database_util.get_score_leaderboard(username)

    if score > current_score:
        database_util.update_score_leaderboard(username, score)

    return jsonify({"success": True, "best_score": max(score, current_score)}), 200


@app.route("/api/v1/best_score", methods=["POST"])
def best_score():
    content = request.json
    if not content:
        return jsonify({"success": False, "error": "Did not specify json body"}), 400
    elif "session_id" not in content:
        return jsonify({"success": False, "error": "session_id id field not present"}), 403

    session_id = content["session_id"]
    session = config.session_manager.get_session(session_id)

    if not session:
        return jsonify({"success": False, "error": "There are no active sessions associated with session_id"}), 403

    username = session.username

    return jsonify({"success": True, "best_score": database_util.get_score_leaderboard(username)}), 200
