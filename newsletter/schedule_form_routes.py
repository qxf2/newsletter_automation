from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template
from . models import NewsletterContent, Newsletter_schedule, AddNewsletter
from . schedule_forms import ScheduleForm, SendTestEmail
from flask import render_template
from newsletter import app
from newsletter import db
from sqlalchemy import desc
from newsletter import csrf
from helpers.mailchimp_helper import Mailchimp_Helper

client = Mailchimp_Helper()


@app.route("/sendtestemail",methods=["GET","POST"])
def schedule_test_email():
    "Scheduling test email"
    newsletter_info = db.session.query(AddNewsletter).order_by(desc(AddNewsletter.newsletter_id)).all()
    newsletter_subject = newsletter_info[0].subject
    test_email_object = SendTestEmail()
    if request.method == 'POST':
        #Discuss with rohan and remove the below two lines
        #newsletter_info = db.session.query(NewsletterContent).order_by(desc(NewsletterContent.newsletter_id)).all()
        #campaign_id = newsletter_info[0].campaign_id
        #Add the mail chimp api call to send test email
        test_emails = ["test@qxf2.com"]
        response = client.send_test_email(test_emails)
        if response == 204:
            flash("Test email has been sent.")
            return redirect('/schedule')
        else:
            flash("Test email has not been sent please try again")

    return render_template('send_test_email.html',sendtestemail=test_email_object,subject=newsletter_subject)


@app.route("/schedule",methods=["GET","POST"])
def schedule_newsletter():
    "Schedule the newsletter"
    newsletter_info = db.session.query(NewsletterContent).order_by(desc(NewsletterContent.newsletter_id)).all()
    newsletter_id = newsletter_info[0].newsletter_id
    campaign_id = newsletter_info[0].campaign_id
    schedule_form_object = ScheduleForm()
    if request.method == 'POST' and schedule_form_object.validate():
        date_to_schedule = schedule_form_object.schedule_date.data
        #Add the mail chimp api call to schedule the newletter
        #Missing items
        #convert the date into utc time
        #time picker 12,12.15,12.30
        #client.schedule_campaign('2021-06-15 08:30:00.00000')
        response = client.schedule_campaign(date_to_schedule)
        if response == 204:
            add_newsletter_schedule = Newsletter_schedule()
            flash("Newsletter has been scheduled")
        else:
            flash("Newsletter is not scheduled")

    return render_template("schedule_newsletter.html",scheduleform=schedule_form_object)
