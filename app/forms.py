from flask_wtf import FlaskForm
from wtforms import StringFiled, PasswordField, BooleanField, SubmitFiled
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringFiled('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')