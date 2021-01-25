from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUp_Form(FlaskForm):
    userName = StringField('Username')
    password = PasswordField('Password')

    submit = SubmitField('Sign Up')