#Flask Form To add Data
#from newsletter.routes import description
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.fields.core import Label, StringField
from wtforms.validators import DataRequired, Length,ValidationError,url
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
    url = URLField('url', validators=[DataRequired(), url()])
    title = TextField('Title')
    description = TextAreaField('Description')
    time = TextField('Time')
    category_id = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name')
    submit = SubmitField('Add Article')
