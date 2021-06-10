"""
This Module Contains the Form classs for newsletter_add
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class Newsletter_AddForm(FlaskForm):
    "Class for Newsletter_Add form"
    subject = StringField('Subject',validators=[DataRequired()])
    preview_text = StringField('Preview Text',validators=[DataRequired()])
    add_article = SubmitField('Add Article')
