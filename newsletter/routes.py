from flask import Flask, request, flash, url_for, redirect, render_template
from newsletter import app
from . models import AddNewsletter, db
from . Newsletter_add_form import Newsletter_AddForm
from . Article_add_form import ArticleForm


@app.route('/')
def index():
    return render_template('home.html')

@app.route("/newsletter",methods=["GET","POST"])
@app.route("/add-newsletter",methods=["GET","POST"])
def Add_newsletter():
    "This page contains the form into which user enters the newsletter subject"
    form = Newsletter_AddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            add_subject = AddNewsletter(form.subject.data)
            db.session.add(add_subject)
            db.session.commit()
            flash(f'Form submitted successfully', 'success')
            return redirect(url_for("Add_articles"))
    return render_template('add_newsletter.html',form=form)

@app.route("/add-articles",methods=["GET","POST"])
def Add_articles():
    "This page contains the form where user can add articles"
    form = ArticleForm(request.form)
    if form.validate_on_submit():
        category=form.category.data
        url= form.url.data
        description=form.description.data
        reading_time=form.reading_time.data
        opener= form.opener.data
        if form.add_more.data:
            file1 = open("replica_db.txt", "a")  # append mode
            file1.write("%s\t%s\t%s\t%s\n"%(category,url,description,reading_time))
            file1.close()
            return redirect(url_for("Add_articles"))
        if form.schedule.data:
            if opener:
                flash(f'Form submitted successfully', 'success')
                return redirect(url_for("index"))
            else:
                flash(f'Please enter the opener')
    return render_template('add_article.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
