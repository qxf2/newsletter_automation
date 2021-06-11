from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config.from_object(__name__)
db = SQLAlchemy(app)


from newsletter import models
from newsletter import routes