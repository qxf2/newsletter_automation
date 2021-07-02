#Flask Form To add Data
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
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
    url= TextField('url', validators= [DataRequired()])
    title = TextField('title', validators= [DataRequired()])
    description = TextField('description', validators= [ DataRequired(), Length(min=4)])
    time = TextField('time',validators=[ DataRequired()])
    category_id = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name')
    submit = SubmitField('Add Article')
