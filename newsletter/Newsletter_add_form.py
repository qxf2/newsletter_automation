"""
This Module Contains the Form classs for newsletter_add
"""
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class Newsletter_AddForm(Form):
    "Class for Newsletter_Add form"
    subject = TextField('subject',validators=[DataRequired()])
    preview_text = StringField('Preview Text',validators=[DataRequired()])
    add_article = SubmitField('Add Article')
