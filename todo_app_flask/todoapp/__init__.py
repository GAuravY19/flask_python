from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3283ccc24be90641ba360ea5fcfdf0bbd6180629c3d80871f444a9ed67fdf752'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.app_context().push()
db = SQLAlchemy(app)


from todoapp import routes