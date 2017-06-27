from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine

basedir = os.path.abspath(os.path.dirname(__file__))

app  = Flask(__name__)
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

db = MongoEngine(app)

Bootstrap(app)
