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

    def does_session_exist(self, session_id):
        return session_id in self.active_sessions

    def clean_sessions(self):
        to_remove = []

        for s in self.active_sessions:
            if time.time() - self.active_sessions[s].last_interacted > self.timeout:  # 30 Minutes
                to_remove.append(s)

        for s in to_remove:
            del self.active_sessions[s]

    def update_session(self, session_id):
        self.active_sessions[session_id].update_last_interacted()


def generate_session_id(username):
    return username + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
