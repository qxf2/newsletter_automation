from flask_wtf import Form
from wtforms import TextField, SubmitField,HiddenField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField



class SendTestEmail(Form):
    newsletter_subject = TextField('newsletter_subject')

class ScheduleForm(Form):
    schedule_date = DateField('DatePicker', format='%Y-%m-%d')

