from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

db_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/newsletter_automation.db'))
app.config['SECRET_KEY'] = "newsletter_automation"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s"%db_file

app.config.from_object(__name__)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
csrf.init_app(app)


from newsletter import models
from newsletter import routes
from newsletter import schedule_form_routes
