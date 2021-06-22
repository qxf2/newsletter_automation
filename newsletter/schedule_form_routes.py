"""
This file is used to send test email from mail chimp and
it schedule the newletter automation also
"""
from flask import request, flash, redirect, render_template
from sqlalchemy import desc
import pytz
from helpers.mailchimp_helper import Mailchimp_Helper
from . models import AddNewsletter, NewsletterContent, Newsletter_schedule
from . schedule_forms import ScheduleForm, SendTestEmail
from newsletter import app
from newsletter import db


client = Mailchimp_Helper()

@app.route("/sendtestemail",methods=["GET","POST"])
def schedule_test_email():
    "Scheduling test email"
    newsletter_list = []
    newsletter_info = db.session.query(AddNewsletter).order_by(
                            desc(AddNewsletter.newsletter_id)).all()

    newsletter_subject = newsletter_info[0].subject
    test_email_object = SendTestEmail()
    if request.method == 'POST':
        #Add the mail chimp api call to send test email
        test_emails = ["test@qxf2.com"]
        response = client.send_test_email(test_emails)
        print(response)
        if response == 204:
            flash("Test email has been sent.")
            return redirect('/schedule')
        else:
            flash(f"Test email has not been sent please try again. The error is  {response}")

    return render_template('send_test_email.html',
                            sendtestemail=test_email_object,
                            subject=newsletter_subject)


def convert_into_utc_format(date_to_schedule):
    "Method converts into UTC format"
    local = pytz.timezone("America/Los_Angeles")
    date_to_schedule = local.localize(date_to_schedule, is_dst=None)
    date_to_schedule = date_to_schedule.astimezone(pytz.utc)
    #We can change the format as per our choice
    date_to_schedule.strftime("%Y-%m-%d %H:%M:%S")

    return date_to_schedule


@app.route("/schedule",methods=["GET","POST"])
def schedule_newsletter():
    "Schedule the newsletter"
    newsletter_info = db.session.query(AddNewsletter).order_by(
                            desc(AddNewsletter.newsletter_id)).all()
    newsletter_id = newsletter_info[0].newsletter_id
    schedule_form_object = ScheduleForm()
    if request.method == 'POST':
        scheduled_date = schedule_form_object.schedule_date.data
        date_to_schedule = convert_into_utc_format(scheduled_date)
        date_to_schedule = date_to_schedule.isoformat()
        #Mailchimp API call to schedule
        response = client.schedule_campaign(date_to_schedule)
        if response == 204:
            add_newsletter_schedule_object = Newsletter_schedule(newsletter_id=newsletter_id,
                                                                schedule_date=date_to_schedule)
            db.session.add(add_newsletter_schedule_object)
            db.session.commit()
            flash(f"Newsletter has been scheduled on {date_to_schedule}")
        else:
            flash(f"Newsletter is not scheduled. Please check the issue {response}")

    return render_template("schedule_newsletter.html",scheduleform=schedule_form_object)
