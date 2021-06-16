from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template
from . models import Newsletter, Newsletter_schedule
from . schedule_forms import ScheduleForm, SendTestEmail
from flask import render_template
from newsletter import app
from newsletter import db
from sqlalchemy import desc
from newsletter import csrf


@app.route("/sendtestemail",methods=["GET","POST"])
def schedule_test_email():
    "Scheduling test email"
    newsletter_info = db.session.query(Newsletter).order_by(desc(Newsletter.newsletter_id)).all()
    newsletter_subject = newsletter_info[0].subject
    test_email_object = SendTestEmail()
    if request.method == 'POST':
        #Add the mail chimp api call to send test email
        flash("Test email has been sent.")
        return redirect('/schedule')
    return render_template('send_test_email.html',sendtestemail=test_email_object,subject=newsletter_subject)


@app.route("/schedule",methods=["GET","POST"])
def schedule_newsletter():
    "Schedule the newsletter"
    newsletter_info = db.session.query(Newsletter).order_by(desc(Newsletter.newsletter_id)).all()
    newsletter_id = newsletter_info[0].newsletter_id
    campaign_id = newsletter_info[0].campaign_id
    schedule_form_object = ScheduleForm()
    if request.method == 'POST' and schedule_form_object.validate():
        date_to_schedule = schedule_form_object.schedule_date.data
        flash("News letter has been scheduled")
    return render_template("schedule_newsletter.html",scheduleform=schedule_form_object)
