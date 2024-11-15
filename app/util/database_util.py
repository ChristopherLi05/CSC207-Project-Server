from app import config


def does_user_exist(username):
    return config.users.find_one({"username": username})


def add_user(username, hashed_pwd):
    config.users.insert_one({"username": username, "password": hashed_pwd})


def does_cred_match(username, password):
    return config.users.find_one({"username": username, "password": password})


def get_top10_leaderboard():
    return [{"username": i["username"], "score": i["score"]} for i in config.leaderboard.find().sort({"score": -1}).limit(10)]


def update_score_leaderboard(username, score):
    config.leaderboard.update_one({"username": username}, {"$set": {"score": score}}, upsert=True)


def get_score_leaderboard(username):
    entry = config.leaderboard.find_one({"username": username})
    return entry["score"] if entry else 0
