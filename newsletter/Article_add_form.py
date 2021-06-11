"""
This Module Contains the Form classes for Add articles form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FormField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class ArticleForm(FlaskForm):
    "Class for articles form"
    categories=["Select Category","Comic","Articles from this week", "Articles from past","Automation corner"]
    category = SelectField('Select_Category', choices=categories,validators=[DataRequired()],default="Select Category")
    title = StringField('Title')
    url = SelectField("Select a url", validate_choice=False)
    description = TextAreaField('Description')
    reading_time = StringField('Reading Time')
    add_more = SubmitField('Add More Articles')
    added_articles = my_field = TextAreaField('Added Articles:', render_kw={'readonly': True})
    opener = TextAreaField('Opener')
    preview_text = TextAreaField('Preview Text',render_kw={'maxlength': 150})
    schedule = SubmitField('Schedule')
