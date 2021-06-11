from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter2.sqlite3'
app.config['SECRET_KEY'] = "random string"

app.config.from_object(__name__)

from newsletter import models
from newsletter import routes

