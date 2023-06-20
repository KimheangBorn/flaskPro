from app.task import *
class Fearture:
    def Feartues():
        Fearture={
        'TForm': useTForm(),
        'CheckDate':CheckDate,
        'ConvertDate':ConvertDate,
        'DateoverDue':DateoverDue,
        'DataTask':DataTask
        }
        return Fearture
class Index:
    # Index
    @main.route('/')
    def index():
        return render_template('index.html.j2')
    
class Profile:
    # profile index
    @main.route('/mytasks/',methods=['GET','POST'])
    @login_required
    def profile():
        status='index'
        return redirect(url_for('main.ActionTasks',status=status))
    # value =overdue/today/notyet/completed/uncompleted
    @main.route('/mytasks/<status>/')
    @login_required
    def ActionTasks(status):
        AllTask=UserTask(status)
        return render_template('profile.html.j2',AllTask=AllTask,**Fearture.Feartues(),status=status)
    # status=value
    # Route Insert
    @main.route('/mytasks/insert/<status>',methods=['GET','POST'])
    @login_required
    def InsertTasks(status):
        TaskName=request.form.get('TaskName')
        Desc=request.form.get('Description')
        Duedate=request.form.get('DueDate')
        insertTask(TaskName,Desc,Duedate)
        return redirect(url_for('main.ActionTasks',status=status))
    # Route Edit and Delete
    @main.route('/mytasks/<taskid>/<str>/<status>',methods=['GET','POST'])
    @login_required
    def PostTasks(taskid,str,status):
        TaskID=taskid
        TaskName=request.form.get('TaskName')
        Desc=request.form.get('Description')
        DueDate=request.form.get('DueDate')
        Check=request.form.get('Check')
        if str=='delete':
            DeleteTask(TaskID)
        elif str=='edit':
            editTask(TaskID,TaskName,Desc,DueDate)
        elif str=='check':
            isCheck(TaskID,Check)
        return redirect(url_for('main.ActionTasks',status=status))

class Filter:      
    @main.route('/filter/',methods=['GET','POST'])
    @login_required
    def FilterTasks():
        Data=''
        DateValue=request.form.get('DateValue')
        Completed=request.form.get('getValue')
        if bool(DateValue):
            Data=DateValue
        elif bool(Completed):
            Data=Completed
        else:
            return redirect(url_for('main.profile'))
        return redirect(url_for('main.ActionTasks',status=Data))
    
