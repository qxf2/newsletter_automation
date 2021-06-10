from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    

class AddArticlesForm(Form):
    dropdown_list = ['a','b','c']
    url = TextField('url', validators=[ DataRequired()])
    title = TextField('title', validators = [DataRequired()])
    description = TextField('Description', validators = [DataRequired()])
    #time = TextField('time', validators = [DataRequired()])
#    category = SelectField('Delivery Types', choices=dropdown_list, default=1)
    #category_id = TextField('category', validators = [DataRequired()])
    submit = SubmitField('Submit')
