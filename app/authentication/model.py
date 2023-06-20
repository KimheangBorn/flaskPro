from flask_login import *
from werkzeug.security import check_password_hash ,generate_password_hash
from app import db ,login_manager
class TODO_USER(UserMixin,db.Model):
	ID= db.Column(db.Integer, primary_key=True,autoincrement=True)
	FirstName= db.Column(db.String(15))
	LastName = db.Column(db.String(15))
	Email= db.Column(db.String(35),unique=True)
	Password = db.Column(db.String(255))
 
	def __init__(self, FirstName, LastName, Email,Password):
		self.FirstName = FirstName
		self.LastName = LastName
		self.Email = Email
		self.Password = generate_password_hash(Password)

	# save
	def saveUser(self,user):
		db.session.add(user)
		db.session.commit()
	# Get ID
	def get_id(self):
           return (self.ID)
@login_manager.user_loader
def load_user(ID):
	return TODO_USER.query.get(int(ID))

