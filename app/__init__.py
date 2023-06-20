from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
# scret key
# database
user_name = "kimheang"
host_name = "localhost"
db_name = "tododb"
pwd = "123456"
port= "5432"
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
app.config['SQLALCHEMY_DATABASE_URI']= f"postgresql://{user_name}:{pwd}@{host_name}:{port}/{db_name}"
db = SQLAlchemy(app)
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)
from app.authentication.views import *
from app.task.main import *
app.register_blueprint(main)