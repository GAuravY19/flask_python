from flask_code import app,db, bcrypt
from flask import Flask, render_template, render_template, flash, redirect, url_for, request
from flask_code.forms import RegistrationForm, LoginForm, code_lang
from flask_sqlalchemy import SQLAlchemy
from flask_code.models import User
from flask_login import login_user, logout_user, login_required, current_user
from flask_code.code_lang import coding, decoding
import random
import string

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf')
        user1 = User(name = form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user1)
        db.session.commit()
        flash("Your Account has been created!", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main_page'))
        else:
            flash("Please check Your email and password", 'danger')
            
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/main_page', methods = ['GET', 'POST'])
@login_required
def main_page():
    form = code_lang()
    if request.method == 'POST':
        msg = form.msg.data
        t = form.target.data
    
        ran_str=string.ascii_lowercase + string.digits
        first = ''.join(random.choice(ran_str) for _ in range(3))
        sec = ''.join(random.choice(ran_str) for _ in range(3))

        if t==1:
            data=coding(msg, first, sec)
            return render_template('main.html',form =form, data=data)
        elif t==0:
            data=decoding(msg)
            return render_template('main.html', form=form, data=data)
        
    return render_template('main.html', form=form )



