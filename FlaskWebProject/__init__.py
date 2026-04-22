"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config.from_object(Config)

# Configure logging for the application
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
app.logger.addHandler(streamHandler)

# Tell Flask it is behind a proxy to ensure HTTPS is sent to Microsoft Entra ID
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views