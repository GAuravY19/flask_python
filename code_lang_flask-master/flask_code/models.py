from flask_code import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable = False, unique = True)
    email = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable=False, unique=True)
    
    