from flask import Flask, request
import os

app = Flask(__name__, template_folder=os.path.abspath(__file__ + "/../templates"), static_folder=os.path.abspath(__file__ + "/../static"))

from app.views import main_routes
