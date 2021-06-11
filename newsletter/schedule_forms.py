from flask_wtf import Form
from wtforms import TextField, SubmitField,HiddenField
from wtforms.validators import DataRequired, Length, Email


class ScheduleForm(Form):
    newsletter_subject = TextField('newsletter_subject', validators= [DataRequired()])
    submit = SubmitField('Send Test Email')
    newsletter_id = HiddenField('newsletter_id')
    campaign_id = HiddenField('campaign_id')
