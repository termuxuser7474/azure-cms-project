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

# 1. ENHANCED LOGGING (Essential for Udacity Rubric & Debugging)
# This will output errors to the Azure Log Stream so you can see the real 500 error
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
app.logger.addHandler(streamHandler)

# 2. PROXY FIX (Ensures Microsoft Login uses HTTPS)
# This tells Flask to trust the Azure headers for SSL
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# 3. INITIALIZE EXTENSIONS
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# 4. DATABASE CONNECTIVITY LOG (Check if DB is reachable on startup)
@app.before_first_request
def test_db_connection():
    try:
        # This tiny query checks if the database is actually reachable
        db.engine.connect()
        app.logger.info("Database connection successful.")
    except Exception as e:
        app.logger.error(f"Database connection failed: {str(e)}")

import FlaskWebProject.views