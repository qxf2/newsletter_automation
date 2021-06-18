"""
This Module Contains the Form classs for newsletter_add
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Newsletter_AddForm(FlaskForm):
    "Class for Newsletter_Add form"
    subject = StringField('Subject',validators=[DataRequired()])
    add_article = SubmitField('Add Article')