from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3283ccc24be90641ba360ea5fcfdf0bbd6180629c3d80871f444a9ed67fdf752'

from todoapp import routes