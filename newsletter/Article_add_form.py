"""
This Module Contains the Form classes for Add articles form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FormField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class ArticleForm(FlaskForm):
    "Class for articles form"
    category = SelectField('Select_Category', choices=["Test1","Test2","Test 3"])
    url = SelectField('URL for article', choices=["Test1","Test2","Test 3"])
    description = TextAreaField('Description',validators=[DataRequired()])
    reading_time = StringField('Reading Time',validators=[DataRequired()])
    add_more = SubmitField('Add More Articles')
    opener = TextAreaField('opener')
    schedule = SubmitField('Schedule')

