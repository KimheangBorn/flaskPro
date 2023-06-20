# # from flask import Flask,redirect,url_for
# # app = Flask(__name__)

# # @app.route('/')
# # def name():
# #    return 'Hello '

# # @app.route("/<name>")
# # def user(name):
# #    return 'hello Narun welcome back How can i help you?!'

# # @app.route("/<admin>")
# # def admin(admin):
# #    return redirect(url_for('hello Administrator,Our system health is currently healthy .')) 

# # if __name__ == '__main__':
# #    #app.debug = True
# #    app.run()
# #    #app.run(debug = True)
# # from flask import Flask
# # import datetime
# # import random

# # app = Flask(__name__)

# # @app.route('/Date/<string:day>')
# # def display_date(day):
# #     current_date = datetime.datetime.now().strftime('%Y-%m-%d')
# #     sentences = ["What a beautiful day!", "It's a good day today!", "Today is not such a great day."]
# #     sentence = random.choice(sentences)
# #     return f"Today is {current_date} - {sentence}"

# # if __name__ == '__main__':
# #     app.run()


# # from flask import Flask;
# # from flask import render_template;

# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return render_template('index.html')
    

# # if __name__ == '__main__':
# #     app.run()
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
# from flask_bcrypt import Bcrypt

app = Flask(__name__)

#user_name = 'superadmin'
# host_name = 'localhost'
# pwd = '    '
# port = '5432'
# db_name = 'tododb'


# app.config['SQLALCHEMY_DATABASE_URI']= f"postgresql://{user_name}:{pwd}@{host_name}:{port}/{db_name}"
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# app.secret_key = ''
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @app.route('/')
# def student():
#    return render_template('index.html')

# @app.route('/register',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("register.html",result = result)
      
# if __name__ == '__main__':
#    app.run()


from app import app

if __name__ == "__main__":
    app.run(debug=True)