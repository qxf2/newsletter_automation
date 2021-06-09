from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    

class AddArticlesForm(Form):
    url = TextField('url', validators=[ DataRequired()])
    title = TextAreaField('title', validators = [DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])
    time = TextAreaField('time', validators = [DataRequired()])
    category = TextAreaField('category', validators = [DataRequired()])

