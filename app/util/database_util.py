from app import config


def does_user_exist(username):
    return config.users.find_one({"username": username})


def add_user(username, hashed_pwd):
    config.users.insert_one({"username": username, "password": hashed_pwd})


def does_cred_match(username, password):
    return config.users.find_one({"username": username, "password": password})
