from wtforms import StringField, SubmitField, PasswordField, EmailField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_code.models import User 

class RegistrationForm(FlaskForm):
    username = StringField("Name :- ", validators=[DataRequired(), Length(min=4, max=10)])
    email =  EmailField("Email :- ", validators=[DataRequired(), Email()])
    password = PasswordField("Password :- ", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password :- ", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Submit")
    
    def validate_username (self,username):
        user = User.query.filter_by(name=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please Take another username.')
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("That email already exists. Please try another")
    

class LoginForm(FlaskForm):
    email =  EmailField("Email :- ", validators=[DataRequired(), Email()])
    password = PasswordField("Password :- ", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
class code_lang(FlaskForm):
    msg = StringField('Message', validators=[DataRequired()])
    target = IntegerField("Enter 1 for coding and 0 for decoding :- ")
    submit = SubmitField("Submit")