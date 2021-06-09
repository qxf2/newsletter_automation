from flask_sqlalchemy import SQLAlchemy
from newsletter import app

db = SQLAlchemy(app)

class articles(db.Model):

   __tablename__ = 'Articles'

   article_id = db.Column('id', db.Integer, primary_key = True)
   url = db.Column(db.String(100))
   title = db.Column(db.String(250))
   description = db.Column(db.String(500))
   time = db.Column(db.String(30))

   def __init__(self, url, title, description, time):
    self.url = url
    self.title = title
    self.description = description
    self.time = time
