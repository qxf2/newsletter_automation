#!/bin/env python
import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/newsletter_automation'
app.config['SQLALCHEMY_BINDS'] = {
    'qa_db': 'mysql+pymysql://root:root@127.0.0.1/qa_db'
}
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

db = SQLAlchemy(app)

# following test db session is for db tests expected verifications
app.config['SQLALCHEMY_DATABASE_TEST_URI'] = 'mysql+pymysql://root:root@127.0.0.1/qa_db'

migrate = Migrate()
migrate.init_app(app, db)

from newsletter import models
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from tests.db_tests import db_tests_models
from newsletter import routes
from newsletter import schedule_form_routes
