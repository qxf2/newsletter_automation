from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    

class AddArticlesForm(Form):
    url= TextField('url', validators= [DataRequired()])
    title = TextField('title', validators= [DataRequired()])
    description = TextField('description', validators= [ DataRequired(), Length(min=4)])
    time = TextField('time',validators=[ DataRequired(), Length(min=6)])
    category_id = SelectField('category', validators= [DataRequired()],choices =[])
    submit = SubmitField('Sign Up')
