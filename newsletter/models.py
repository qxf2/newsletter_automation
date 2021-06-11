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


class Newsletter(db.Model):
    "creating newletter"
    newsletter_id = db.Column('newsletter_id',db.Integer,primary_key=True)
    subject = db.Column('subject',db.String)
    opener = db.Column('opener',db.String)
    category_id = db.Column('category_id',db.Integer,db.ForeignKey(Article_category.category_id))
    articles_id = db.Column('articles_id',db.Integer)
    campaign_id = db.Column('campaign_id',db.Integer)

class Newsletter_schedule(db.Model):
    "Newsletter schedule table"
    schedule_id = db.Column('schedule_id', db.Integer, primary_key=True)
    newsletter_id = db.Column('newsletter_id',db.Integer,db.ForeignKey(Newsletter.newsletter_id))
    schedule_date = db.Column('schedule_date',db.Integer)

    def __init__(self,schedule_id,newsletter_id,schedule_date):
        self.schedule_id = schedule_id
        self.newsletter_id = newsletter_id
        self.schedule_date = schedule_date

db.create_all()
