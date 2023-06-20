from datetime import *
from app.task.TaskForm import TaskForm    
from flask import Blueprint, redirect, render_template, url_for,request
from flask_login import login_required
from app.task.model import *
main = Blueprint('main', __name__)
def CheckDate(CurDate):
    if not CurDate==None:
        Current=str(CurDate.strftime("%d-%m-%Y"))
        Today = str(date.today().strftime("%d-%m-%Y"))
        Tomorow = str((date.today() + timedelta(1)).strftime("%d-%m-%Y"))
        Tag=''
        if Current==Today:
            Tag='Today'
        elif Current==Tomorow:
            Tag='Tomorow'
        else:
            Tag=str(CurDate.strftime("%d/%m/%Y"))
        return Tag
        
# Date Convert
def ConvertDate(date):
    EditDate=str(date.strftime("%Y-%m-%d"))
    return EditDate

# change color date overdue
def DateoverDue(Date):
    if not Date==None:
        TaskDate=Date
        Today = date.today()
        if TaskDate>=Today:
            return 'text-bg-success'
        return 'text-bg-danger'
    
def useTForm():
    TForm=TaskForm(request.form)
    return TForm

def DataTask(Alltask):
    Data=list(Alltask)
    return Data
    
    
    
    