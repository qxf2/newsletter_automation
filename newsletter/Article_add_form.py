"""
This Module Contains the Form classes for Add articles form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FormField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category,Articles,db
from sqlalchemy.orm import sessionmaker

def choice_query():
    "Subquery for the QuerySelectField"
    return Article_category.query

class ArticleForm(FlaskForm):
    "Class for articles form"
    
    
    category_id= QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name')
    url = SelectField("Select a url", validate_choice=False)
    title = StringField('Title', render_kw ={'readonly':True})
    description = TextAreaField('Description',render_kw ={'readonly':True})
    reading_time = StringField('Reading Time', render_kw ={'readonly':True})
    add_more = SubmitField('Add More Articles')
    subject = StringField('Subject')
    added_articles = my_field = TextAreaField('Added Articles:', render_kw={'readonly': True})
    opener = TextAreaField('Opener')
    preview_text = TextAreaField('Preview Text',render_kw={'maxlength': 150})
    schedule = SubmitField('Schedule')
    cancel = SubmitField('Cancel')
