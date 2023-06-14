from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, EmailField, PasswordField, TextAreaField 
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username :- ", validators=[DataRequired()])
    email = EmailField("Email :- ", validators=[DataRequired(), Email()])
    password = PasswordField("Password :- " , validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password :- ", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Submit")
    

class LoginForm(FlaskForm):
    email = EmailField("Email :- ", validators=[DataRequired(), Email()])
    password = PasswordField("Password :- " , validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
class Addtodo(FlaskForm):
    title = TextAreaField('Todo Title :- ', validators=[DataRequired()])
    description = TextAreaField('Todo Description :- ', validators=[DataRequired()])
    add = SubmitField("Add")