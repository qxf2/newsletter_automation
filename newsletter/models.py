from flask_sqlalchemy import SQLAlchemy
from newsletter import app

db = SQLAlchemy(app)

class Articles(db.Model):

   article_id = db.Column('id', db.Integer, primary_key = True)
   url = db.Column(db.String(100))
   title = db.Column(db.String(250))
   description = db.Column(db.String(500))
#   time = db.Column(db.Integer)
#   category_id = db.Column(db.Integer, db.ForeignKey('article_category.id'))

   def __init__(self, url, title, description, time,category_id):
    self.url = url
    self.title = title
    self.description = description
#    self.time = time
#    self.category_id = category_id

class Article_category(db.Model):
    category_id = db.Column('id', db.Integer, primary_key = True)
    category_name = db.Column(db.String(100))

    def __init__(self, category_name):
        self.category_name = ['this week', 'previous week', 'comic','automation']

#ins = Article_category.insert().values([{category_name:'this week'},{category_name:'previous week'},{category_name:'comic'},{category_name:'automation'}])

db.create_all()
