import random
import pandas as pd
import os
import time
import json
from app.app import app, db, mail
from app.user import User, Role
from app.forms.forms import TextingForm
from flask import request, render_template, session, url_for, redirect
from flask_security import Security, MongoEngineUserDatastore, login_required, current_user
from app.send_email import send_email
from app.modules.view_functions import validate_list, message_list

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)
security.send_mail_task(send_email)

# Views
@app.route('/', methods=['GET','POST'])
@login_required
def home():
    form = TextingForm()
    if form.validate_on_submit():
        textingList = form.textingList.data
        df = pd.read_csv(textingList)
        if validate_list(df):
            message_list(df, current_user.id)
        else:
            flash("Your CSV is an incorrect format")
    return render_template('/index.jade', texting_form = form)
