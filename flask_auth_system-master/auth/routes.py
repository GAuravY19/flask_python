from flask import render_template,url_for, redirect, flash, request
from auth.forms import RegistrationForm, LoginForm
from auth import app , bcrypt, db
from auth.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 


@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user1=User(username = form.username.data, email = form.email.data, password = hashed_pw)
        db.session.add(user1)
        db.session.commit()
        flash("You have registered successfully", 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('loggedin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('loggedin'))
        else:
            flash('login unsuccessful! Please check email and password')
        
    return render_template('login.html', form=form)


@app.route('/account')
@login_required
def account():
    return render_template('account.html')


@app.route('/loggedin')
@login_required
def loggedin():
    return render_template('loggedin.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('home')