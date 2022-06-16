#!/bin/env python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
db_user = os.environ.get("MYSQL_USERNAME","root")
db_password = os.environ.get("MYSQL_PASSWORD","root")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@127.0.0.1/newsletter_automation'
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET","random string")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db)

from newsletter import models
from newsletter import routes
from newsletter import schedule_form_routes
