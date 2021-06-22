from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField,HiddenField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateTimeLocalField



class SendTestEmail(FlaskForm):
    newsletter_subject = TextField('newsletter_subject')

class ScheduleForm(FlaskForm):
    schedule_date = DateTimeLocalField('schedule_date', format='%Y-%m-%dT%H:%M')


