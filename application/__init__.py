from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

from application import routes
