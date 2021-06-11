#Creating Db Schema
from flask_sqlalchemy import SQLAlchemy
from newsletter import app


db = SQLAlchemy(app)

class Articles(db.Model):
   article_id = db.Column('article_id', db.Integer, primary_key = True)
   url = db.Column(db.String(100))
   title = db.Column(db.String(250))
   description = db.Column(db.String(500))
   time = db.Column(db.String(300))
   category_id = db.Column(db.Integer, db.ForeignKey('article_category.category_id'))

   def __init__(self, url, title, description, time,category_id):
    self.url = url
    self.title = title
    self.description = description
    self.time = time
    self.category_id = category_id

class Article_category(db.Model):
    category_id = db.Column('category_id', db.Integer, primary_key = True)
    category_name = db.Column(db.String(100))

    def __init__(self, category_name):
        self.category_name = category_name

    def __repr__(self):
        return '<Article_category {}'.format(self.category_name)

db.create_all()
