from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email , Length, EqualTo, ValidationError
from auth.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField("Email", validators=[DataRequired(), Length(min=6, max=50), Email()] )
    password = PasswordField("Password", validators=[DataRequired()] )
    confirm_pw = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    check = BooleanField("I agree all statements in")
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        username = User.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('That username is taken. Please try another.')
    
    
    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('That email is taken. Please a another one.')
    
    
    
class LoginForm(FlaskForm):
    email = EmailField("Email",  validators=[DataRequired(), Email(), Length(min=6, max=50)])
    password = PasswordField("Password", validators=[DataRequired()] )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')