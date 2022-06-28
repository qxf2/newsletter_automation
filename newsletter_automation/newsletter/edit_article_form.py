"""Flask Form To edit articles"""
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField,SelectField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category

def fetch_categories():
    "This is for category to get value for choices used by category_id selectfield"
    categories = Article_category.query
    categoryarray=[]
    for each_category in categories:
        category_obj={}
        category_obj['id'] = each_category.category_id
        category_obj['category_name'] =each_category.category_name
        choice_tuple=(category_obj['id'],category_obj['category_name'])
        categoryarray.append(choice_tuple)
    return categoryarray

class EditArticlesForm(FlaskForm):
    "To edit articles data"
    url= TextField('url', validators= [DataRequired()])
    title = TextField('title', validators= [DataRequired()])
    description = TextAreaField('description', validators= [ DataRequired(), Length(min=4)])
    time = TextField('time',validators=[ DataRequired()])
    category_id= SelectField(choices=fetch_categories())
    submit = SubmitField('Save')
