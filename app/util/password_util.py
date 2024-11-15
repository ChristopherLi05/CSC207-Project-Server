import hashlib
from app.config import SALT


def hash_password(pwd: str):
    return hashlib.sha256((pwd + SALT).encode("utf-8")).hexdigest()
