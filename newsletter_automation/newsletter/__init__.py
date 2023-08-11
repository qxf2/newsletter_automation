#!/bin/env python
import os
import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask import Blueprint
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
flask_metrics = PrometheusMetrics(app)
db_user = os.environ.get("MYSQL_USERNAME","root")
db_password = os.environ.get("MYSQL_PASSWORD","root")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{urllib.parse.quote(db_password)}@127.0.0.1/newsletter_automation'
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET","random string")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db)

metrics = Blueprint("metrics", __name__)

from newsletter import models
from newsletter import routes
from newsletter import schedule_form_routes
app.register_blueprint(metrics)
