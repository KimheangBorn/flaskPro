# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

# from app.authentication.model import USER

# class SignInForm(FlaskForm):
#     # username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
#     Email = StringField('Email', validators=[DataRequired('Email Required'), Email()])
#     Password = PasswordField('Password', validators=[DataRequired('Password Required')])
#     # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')
    
    # def validate_username(self, username):
    #     user = USER.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('Username is already taken!')
        
    # def validate_email(self, email):
    #     user = USER.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('Email is already registered!')
from wtforms import SubmitField, StringField, PasswordField, validators,ValidationError
from flask_wtf import FlaskForm
from .model import *
                    
class SignInForm(FlaskForm):
  Email = StringField('Email',validators=[validators.InputRequired('Email Required'),validators.Email()])
  Password = PasswordField('Password',validators=[validators.InputRequired('Password Required')])
  submit = SubmitField('Login')
  #username = ValidationError('error')