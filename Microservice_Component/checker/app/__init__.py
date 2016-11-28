from flask import Flask

app = Flask(__name__)

from app import tasks, check_range