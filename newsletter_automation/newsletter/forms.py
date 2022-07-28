#Flask Form To add Data
#from newsletter.routes import description
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.fields.core import Label, StringField
from wtforms.validators import DataRequired, Length,ValidationError,url, Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category

#Check for fields not empty
def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')

#This is for category to get value for query_factory used by QuerySelectField
def choice_query():
    return Article_category.query

#To add articles data
class AddArticlesForm(FlaskForm):
    url = URLField('url', validators=[DataRequired(message="URL cannot be blank"), url(message='Invalid URL pattern'), Regexp('^(http|https)://', message='Invalid URL. URL should start with http(s)://'), Length(max=512, message='URL should be less than 512 characters')])
    title = TextField('Title', validators=[DataRequired(message="Title cannot be blank"), Length(max=250, message='Title should be less than 250 characters')])
    description = TextAreaField('Description', validators=[DataRequired(message="Description cannot be blank"), Length(max=500, message='Description should be less than 500 characters')])
    time = TextField('Time', validators=[Regexp('^[1-9]\d*$', message='Time should be an integer greater than 0'), DataRequired(message="Time field cannot be blank")])
    category_id = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name', validators=[DataRequired(message="Category cannot be blank")])
    submit = SubmitField('Add Article')
    article_editor = TextField('Article Editor')
