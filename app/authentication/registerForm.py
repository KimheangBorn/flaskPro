from wtforms import SubmitField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from .model import *
from app import db 

# checking Email 
def validate_email(form,field):
      Email=db.session.query(TODO_USER).filter(TODO_USER.Email==field.data)
      Email_DB=''
      for item in Email:
          Email_DB=item.Email
      if Email_DB==field.data:
          raise validators.ValidationError('Your Email has Registered!')     
           
# RegisterForm
class Register_Form(FlaskForm):
  FirstName = StringField('First Name', 
                  [validators.InputRequired('First Name required')])
  LastName = StringField('Last Name', 
                  [validators.InputRequired('Last Name required')])
  Email = StringField('Email Address',
                  [validators.InputRequired('Email required'),validators.Email(),validate_email])
  Password = PasswordField('Enter Password',
                  [validators.InputRequired('Password required'),validators.EqualTo(fieldname='Comfirm', 
                  message='Passwords must match'),validators.Length(min=8)
        ])
  Comfirm = PasswordField('Comfirm Password',
                          [validators.InputRequired('Password Comfirm required'),validators.Length(min=8)])
  Submit = SubmitField('Signup')
