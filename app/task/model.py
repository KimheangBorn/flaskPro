from datetime import date
from flask_login import current_user
from app import db
class TASK_LIST(db.Model):
    TaskID= db.Column(db.Integer, primary_key=True,autoincrement=True)
    TaskName= db.Column(db.String(100))
    Description = db.Column(db.String(255))
    DueDate= db.Column(db.Date)
    Check = db.Column(db.Boolean)
    UserID = db.Column(db.Integer,default=True)
    CreatedDate=db.Column(db.TIMESTAMP,nullable=False,server_default=db.func.now(),onupdate=db.func.now())

    def __init__(self, TaskName,Description,DueDate,Check,UserID):
        self.TaskName=TaskName
        self.Description=Description
        self.DueDate=DueDate
        self.Check=Check
        self.UserID=UserID
        
# filter Task
def UserTask(Status='index'):
    Task=TASK_LIST.query.filter_by(UserID=current_user.ID)
    # Tasks of all times
    AllTask=[]

    
    if Status=='today':
        AllTask=Task.filter_by(Check=False,DueDate=date.today()).order_by(TASK_LIST.CreatedDate.desc())
        # OverDue
    elif Status=='overdue':
        AllTask=Task.filter_by(Check=False).filter(TASK_LIST.DueDate<date.today()).order_by(TASK_LIST.CreatedDate.desc())
        # Not Yet Do
    elif Status=='notyet':
        AllTask=Task.filter_by(Check=False).filter(TASK_LIST.DueDate>date.today()).order_by(TASK_LIST.CreatedDate.desc())              
        # complete
    elif Status=='completed':
        AllTask=Task.filter_by(Check=True).order_by(TASK_LIST.CreatedDate.desc())
        # uncomplete
    elif Status=='uncompleted':
        AllTask=Task.filter_by(Check=False).filter(TASK_LIST.DueDate>date.today()).order_by(TASK_LIST.CreatedDate.desc())  
    elif Status=='index':
        AllTask=Task.filter_by(Check=False).order_by(TASK_LIST.CreatedDate.desc())         
    return AllTask
# Insert
def insertTask(TaskName,Description,DueDate):
    UserID=current_user.ID
    newTask = TASK_LIST(TaskName,Description,DueDate,False,UserID)
    db.session.add(newTask)
    db.session.commit()
    
#  Edit
def editTask(TaskID,TaskName,Description,DueDate):
    Task=TASK_LIST.query.filter_by(TaskID=TaskID).one()
    Task.TaskName=TaskName
    Task.Description=Description
    Task.DueDate=DueDate
    db.session.commit()
    
# Delete   
def DeleteTask(TaskID):
    DeleteTask= TASK_LIST.query.filter_by(TaskID=TaskID).one()
    db.session.delete(DeleteTask)
    db.session.commit()
    
 # Check
def isCheck(TaskID,Check):
    Task=TASK_LIST.query.filter_by(TaskID=TaskID).one()
    Task.Check=bool(Check)
    db.session.commit()


