#!/bin/env python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

USERNAME = os.getenv('MYSQL_USERNAME')
PASSWORD = os.getenv('MYSQL_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@127.0.0.1/newsletter_automation' % (USERNAME, PASSWORD)
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

db = SQLAlchemy(app)

from newsletter import models
from newsletter import routes
from newsletter import schedule_form_routes
