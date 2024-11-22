from flask import Flask
from flask_apscheduler import APScheduler
import os

app = Flask(__name__, template_folder=os.path.abspath(__file__ + "/../templates"), static_folder=os.path.abspath(__file__ + "/../static"))

scheduler = APScheduler()

import app.config as config
scheduler.add_job(func=config.session_manager.clean_sessions, id="session_cleaner", trigger="interval", minutes=10)
scheduler.start()

from app.views import main_routes, login_signup_routes, leaderboard_routes
