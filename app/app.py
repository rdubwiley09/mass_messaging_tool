from flask import Flask
import os
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app  = Flask(__name__)
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

bcrypt = Bcrypt(app)

mongo = PyMongo(app)

Bootstrap(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"
