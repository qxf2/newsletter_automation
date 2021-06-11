from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category


def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    
def choice_query():
    return Article_category.query

class AddArticlesForm(FlaskForm):
    url= TextField('url', validators= [DataRequired()])
    title = TextField('title', validators= [DataRequired()])
    description = TextField('description', validators= [ DataRequired(), Length(min=4)])
    time = TextField('time',validators=[ DataRequired()])
#    category_id = SelectField('category',id ='category_id')
    category_id = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name')
    submit = SubmitField('Add Article')
