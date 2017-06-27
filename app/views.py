import random
import pandas as pd
import os
import time
import json
from app.app import app, mongo, bcrypt
from flask import request, render_template, session, url_for, redirect
from app.forms.forms import LoginForm, RegisterForm
from flask_login import login_required, login_user, logout_user

@app.route("/", methods=['GET','POST'])
@login_required
def index():
    return 'You are logged in'

@app.route('/login', methods=['POST','GET'] )
def login():
    form = LoginForm()
    if request.method == 'POST':
        users = mongo.db.users
        loginUser = users.find_one({'name': form.username.data})
        if loginUser:
            if bcrypt.check_password_hash(loginUser['password'], form.password.data.encode('utf-8')):
                login_user()
                return redirect(url_for('index'))
            else:
                return 'Invalid username/password combination'
        else:
            return 'please register'


    else:
        return render_template('login.jade', form=form)

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        users = mongo.db.users
        existing = users.find_one({'name': form.username.data})
        if existing is None:
            hashpwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            users.insert({'name': form.username.data, 'password': hashpwd})
            session['username'] = form.username.data
            return redirect(url_for('index'))
        else:
            return 'That username already exists'
    else:
        return render_template('register.jade', form=form)

@app.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('index'))
