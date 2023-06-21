from wtforms import SubmitField, StringField, validators,TextAreaField,DateField
from flask_wtf import FlaskForm
from .model import *
def validate_field(form,field):
    if len(field.data)<=200:
        raise validators.ValidationError('You can not writing more than 200!.')     
class TaskForm(FlaskForm):
  TaskName = StringField('Task Name',validators=[validators.InputRequired('Task Name Required.'),validators.Length(max=30)])
  Description = StringField('Task Description',validators=[validators.InputRequired('Task Description Required.'),validators.Length(max=100)])
  DueDate = DateField('DueDate',validators=[validators.InputRequired('DueDate Required.')],default=date.today(),render_kw={'min':date.today()})
  Submit=SubmitField('Create')