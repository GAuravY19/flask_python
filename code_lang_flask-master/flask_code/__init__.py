from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c214ba4b775befe5ff6aff1c4d5e74d6'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:/// first.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.app_context().push()

from flask_code import routes