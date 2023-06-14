from flask import Flask, render_template
from todoapp import app
from todoapp.forms import RegistrationForm, LoginForm, Addtodo



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form = form)


@app.route('/add', methods = ['GET', 'POST'])
def addtodo():
    form = Addtodo()
    return render_template('todo_add.html', form = form)


@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = Addtodo()
    return render_template('update.html', form = form)


@app.route('/delete')
def delete():
    return "Hellow world"


@app.route('/logout')
def logout():
    return "Logout user"
