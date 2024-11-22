import time
import random


class Session:
    def __init__(self, username, session_id):
        self.username = username
        self.session_id = session_id
        self.last_interacted = time.time()

    def update_last_interacted(self):
        self.last_interacted = time.time()


class SessionManager:
    def __init__(self, timeout=60 * 30):
        self.active_sessions: dict[str, Session] = {}
        self.timeout = timeout  # 30 minutes

    def create_session(self, username):
        session_id = generate_session_id(username)
        self.active_sessions[session_id] = Session(username, session_id)
        return session_id

    def get_session(self, session_id):
        self.update_session(session_id)
        return self.active_sessions.get(session_id)

    def clean_sessions(self):
        to_remove = []

        for s in self.active_sessions:
            if time.time() - self.active_sessions[s].last_interacted > self.timeout:  # 30 Minutes
                to_remove.append(s)

        for s in to_remove:
            del self.active_sessions[s]

    def update_session(self, session_id):
        self.active_sessions[session_id].update_last_interacted()


class DBSessionManager:
    def __init__(self, session_db, timeout=60 * 30):
        self.session_db = session_db
        self.timeout = timeout  # 30 minutes

    def create_session(self, username):
        session_id = generate_session_id(username)
        self.session_db.insert_one({"username": username, "session_id": session_id, "last_interacted": time.time()})
        return session_id

    def get_session(self, session_id):
        s = self.session_db.find_one({"session_id": session_id})
        if not s:
            return None

        self.update_session(session_id)
        return Session(s["username"], s["session_id"])

    def clean_sessions(self):
        self.session_db.delete_many({"value": {"$lt", time.time() - self.timeout}})

    def update_session(self, session_id):
        self.session_db.update_one({"session_id": session_id}, {"$set": {"last_interacted": time.time()}})


def generate_session_id(username):
    return username + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=16))
