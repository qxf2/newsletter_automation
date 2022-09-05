"""
This Module Contains the Form classes for Add articles form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category

def choice_query():
    "Subquery for the QuerySelectField"
    return Article_category.query

class ArticleForm(FlaskForm):
    "Class for articles form"


    category_id= QuerySelectField('Category',query_factory=choice_query, allow_blank=True,get_label='category_name')
    url = SelectField("URL", validate_choice=False)
    title = StringField('Title', render_kw ={'readonly':True})
    description = TextAreaField('Description',render_kw ={'readonly':True})
    reading_time = StringField('Reading Time', render_kw ={'readonly':True})
    add_more = SubmitField('Add More Articles')
    subject = StringField('Subject',render_kw={'placeholder': 'Just the date in dd-mmm-yyyy'})
    added_articles = my_field = TextAreaField('Added Articles:', render_kw={'readonly': True})
    opener = TextAreaField('Opener',render_kw={'placeholder': 'Do NOT include the string "In this issue: "'})
    preview_text = TextAreaField('Preview Text',render_kw={'maxlength': 150})
    #schedule = SubmitField('Schedule')
    preview_newsletter = SubmitField('Preview Newsletter')
    cancel = SubmitField('Clear Fields')
