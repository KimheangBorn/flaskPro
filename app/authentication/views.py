from flask import flash, redirect, render_template, request, url_for
from app.authentication.model import *
from .loginForm import SignInForm
from .registerForm import Register_Form
from app import app

# login
@app.route('/login',methods=['GET', 'POST'])
def Login():
    #checking if user has logiging redirect to Index
    if  current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # Login User
    form = SignInForm(request.form)
    if form.validate_on_submit():
        Email=request.form.get('Email')
        Password=request.form.get('Password')
        User=TODO_USER.query.filter_by(Email=Email).first()
        if not User or not check_password_hash(User.Password, Password):
            flash( 'Your Email or Password are Invaid Please try again!.','error')
            return redirect(url_for('Login'))
        login_user(User)
        return redirect(url_for('main.profile'))
    return render_template('login.html.j2', form=form)

# Register
@app.route('/register',methods=['GET', 'POST'])

def Register():
    #checking if user has logiging redirect to Index
    if  current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # Register User
    form = Register_Form(request.form)
    if form.validate_on_submit():
        FirstName=request.form.get('FirstName')
        LastName=request.form.get('LastName')
        Email=request.form.get('Email')
        Password=request.form.get('Password')
        user=TODO_USER(FirstName,LastName,Email,Password)
        user.saveUser(user)
        flash( f'Welcome to Todo ListApp {FirstName},{LastName}','success')
        User=TODO_USER.query.filter_by(Email=Email).first()
        login_user(User)
        return redirect(url_for('main.profile'))
    return render_template('register.html.j2', form=form)

# logout
@app.route('/logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('main.index'))











