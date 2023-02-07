"""
This Module Contains the Form classes for Add articles form
"""
from email import message
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length,ValidationError,url, Regexp
from . models import Article_category

def choice_query():
    "Subquery for the QuerySelectField"
    return Article_category.query

class ArticleForm(FlaskForm):
    "Class for articles form"


    category_id= QuerySelectField('Category',query_factory=choice_query, allow_blank=True,get_label='category_name')
    url = SelectField("url", validate_choice=False)
    title = StringField('Title', render_kw ={'readonly':True})
    description = TextAreaField('Description',render_kw ={'readonly':True})
    reading_time = StringField('Reading Time', render_kw ={'readonly':True})
    add_more = SubmitField('Add More Articles')
    subject = StringField('Subject',render_kw={'placeholder': 'Just the date in dd-mmm-yyyy'}, validators=[Regexp('^\d\d-[A-Z][a-z][a-z]-\d\d\d\d', message='Invalid Subject. Subject should be of form dd-MMM-YYY E.g.: 15-Aug-1947'), Length(min=11, max=11, message='Subject should be exactly 11 characters long. Subject should be of form dd-MMM-YYY E.g.: 15-Aug-1947')])
    added_articles = my_field = TextAreaField('Added Articles:', render_kw={'readonly': True})
    opener = TextAreaField('Opener',render_kw={'placeholder': 'Do NOT include the string "In this issue: "'}, validators=[Length(min=150, max=400, message='Opener should be between 150 and 399 characters long')])
    preview_text = TextAreaField('Preview Text',render_kw={'maxlength': 150}, validators=[Length(min=70, max=150, message='Preview should be between 70 and 150 characters long')])
    preview_newsletter = SubmitField('Preview Newsletter')
    cancel = SubmitField('Clear Fields')
