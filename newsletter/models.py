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
    newsletter_id = db.Column(db.Integer, db.ForeignKey('add_newsletter.category_id'))
    category_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)
    campaign_id= db.Column(db.Integer)
    

    def __init__(self, newsletter_id, category_id, article_id, campaign_id):
        self.newsletter_id = newsletter_id
        self.category_id = category_id
        self.article_id = article_id
        self.campaign_id = campaign_id

class Article_category(db.Model):
    category_id = db.Column('category_id', db.Integer, primary_key = True)
    category_name = db.Column(db.String(100))

    def __init__(self, category_name):
        self.category_name = category_name
        
db.create_all()