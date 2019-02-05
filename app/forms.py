from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#part of the user registration
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
 
 #class to allow users to register on the web
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('I want In!')

# restrict Users from using the same details to registor
    def validate_username(self, username):
         user = User.query.filter_by(username=username.data).first()
         if user is not None:
             raise ValidationError('Please use a different username')
     
    def validate_email(self,email): 
         user = User.query.filter_by(email=email.data).first()
         if user is not None:
             raise ValidationError('Please entre the another email address')

          