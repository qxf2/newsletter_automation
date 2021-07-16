from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/newsletter_automation'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(__name__)

db = SQLAlchemy(app)


from newsletter import models
from newsletter import routes
from newsletter import schedule_form_routes