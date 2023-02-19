from flask import Flask
# import config class and import and initialize flask_mail
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
from app import views
