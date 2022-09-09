"""
Models for the Newsletter Automation app
"""

from email.policy import default
from newsletter import db

class AddNewsletter(db.Model):
    "Class for AddNewsletter db model"
    __tablename__ = 'add_newsletter'
    newsletter_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    opener = db.Column(db.String(400))
    preview = db.Column(db.String(400))
    #campaign_id= db.Column(db.Integer)

    def __init__(self, subject, opener,preview):
        "initialize subject,opener"
        self.subject = subject
        self.opener = opener
        self.preview = preview

class NewsletterContent(db.Model):
    "Class for NewsletterContent db model"
    __tablename__ = 'newsletter_content'
    newsletter_content_id = db.Column(db.Integer, primary_key=True)
    newsletter_id = db.Column(db.Integer, db.ForeignKey('add_newsletter.newsletter_id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.article_id'))

    def __init__(self, newsletter_id,  article_id):
        self.newsletter_id = newsletter_id
        self.article_id = article_id

class Articles(db.Model):
    "Class for Article db model"
    article_id = db.Column('article_id', db.Integer, primary_key = True)
    url = db.Column(db.String(512))
    title = db.Column(db.String(250))
    description = db.Column(db.String(500))
    time = db.Column(db.String(300))
    category_id = db.Column(db.Integer, db.ForeignKey('article_category.category_id'))
    newsletter_id = db.Column(db.Integer, db.ForeignKey('add_newsletter.newsletter_id'))
    article_editor = db.Column(db.String(100), default = None)

    def __init__(self, url, title, description, time,category_id, article_editor):
        "initializes url, title, description, time, category_id, article_editor"
        self.url = url
        self.title = title
        self.description = description
        self.time = time
        self.category_id = category_id
        self.article_editor = article_editor


class Article_category(db.Model):
    "Class for Article_category db model"
    __tablename__ = 'article_category'
    category_id = db.Column('category_id', db.Integer, primary_key = True)
    category_name = db.Column(db.String(100))

    def __init__(self, category_name):
        "initializes category_name"
        self.category_name = category_name


class Newsletter_schedule(db.Model):
    "Newsletter schedule table"
    schedule_id = db.Column('schedule_id', db.Integer, primary_key=True)
    newsletter_id = db.Column('newsletter_id',db.Integer,db.ForeignKey('add_newsletter.newsletter_id'))
    schedule_date = db.Column('schedule_date',db.Integer)

    def __init__(self,schedule_id,newsletter_id,schedule_date):
        self.schedule_id = schedule_id
        self.newsletter_id = newsletter_id
        self.schedule_date = schedule_date

class Newsletter_campaign(db.Model):
    "Newsletter create campaign table"
    Newsletter_campaign_id =db.Column('Newsletter_campaign_id', db.Integer, primary_key=True)
    campaign_id = db.Column('campaign_id', db.String(50))
    newsletter_id = db.Column('newsletter_id',db.Integer,db.ForeignKey('add_newsletter.newsletter_id'))

    def __init__(self,campaign_id,newsletter_id):
        self.campaign_id = campaign_id
        self.newsletter_id = newsletter_id

db.create_all()
