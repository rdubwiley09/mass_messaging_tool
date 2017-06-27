import random
import pandas as pd
import os
import time
import json
from app.app import app, db, mail
from app.user import User, Role
from app.forms.forms import LoginForm, RegisterForm
from flask import request, render_template, session, url_for, redirect
from flask_security import Security, MongoEngineUserDatastore, login_required

def test(msg):
    print(dir(msg))
    print(msg.body)

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)
security.send_mail_task(test)

# Views
@app.route('/')
@login_required
def home():
    return 'you did it'
