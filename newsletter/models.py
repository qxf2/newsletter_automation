from flask_sqlalchemy import SQLAlchemy
from newsletter import app
from newsletter import db

class AddNewsletter(db.Model):
    newsletter_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

    def __init__(self, campaign_id, subject):
        self.newsletter_id = newsletter_id
        self.subject = subject

db.create_all()