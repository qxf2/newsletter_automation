from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template
from . models import Newsletter, Newsletter_schedule
from . schedule_forms import ScheduleForm
from flask import render_template
from newsletter import app
from newsletter import db
from sqlalchemy import desc



@app.route("/schedule",methods=["GET","POST"])
def schedule_test_email():
    "Scheduling test email"
    newsletter_info = db.session.query(Newsletter).order_by(desc(Newsletter.newsletter_id)).all()
    newsletter_subject = newsletter_info[0].subject
    newsletter_id = newsletter_info[0].newsletter_id
    campaign_id = newsletter_info[0].campaign_id
    print(newsletter_id,campaign_id,newsletter_subject)
    schedule_form_object = ScheduleForm(request.values,newsletter_id=newsletter_id,campaign_id=campaign_id)

    if request.method == 'POST':
        print("hi how are you")

    return render_template('schedule_form.html',scheduleform=schedule_form_object,subject=newsletter_subject)

