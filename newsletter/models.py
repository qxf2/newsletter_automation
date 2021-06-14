from flask_sqlalchemy import SQLAlchemy
from newsletter import app
from newsletter import db

class AddNewsletter(db.Model):
    __tablename__ = 'add_newsletter'
    newsletter_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    opener = db.Column(db.String(400))
    preview = db.Column(db.String(400))
    
    def __init__(self, subject, opener, preview):
        #self.newsletter_id = newsletter_id
        self.subject = subject
        self.opener = opener
        self.preview = preview


class NewsletterContent(db.Model):
    __tablename__ = 'newsletter_content'
    newsletter_content_id = db.Column(db.Integer, primary_key=True)
    newsletter_id = db.Column(db.Integer, db.ForeignKey('add_newsletter.newsletter_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('article_category.category_id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.article_id'))
    campaign_id= db.Column(db.Integer)
    

    def __init__(self, newsletter_id, category_id, article_id, campaign_id):
        self.newsletter_id = newsletter_id
        self.category_id = category_id
        self.article_id = article_id
        self.campaign_id = campaign_id

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
    
   def __repr__(self):
        return '<Articles {}'.format(self.url)

class Article_category(db.Model):
    __tablename__ = 'article_category'
    category_id = db.Column('category_id', db.Integer, primary_key = True)
    category_name = db.Column(db.String(100))

    def __init__(self, category_name):
        self.category_name = category_name
        
    def __repr__(self):
        return '<Article_category {}'.format(self.category_name)
        
db.create_all()