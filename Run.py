
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= f"postgresql://{user_name}:{pwd}@{host_name}:{port}/{db_name}"
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# app.secret_key = ''
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


from app import app

if __name__ == "__main__":
    app.run(debug=True)