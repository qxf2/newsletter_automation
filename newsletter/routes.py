from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from newsletter import app
from . models import AddNewsletter, db, Article_category, Articles
from . Newsletter_add_form import Newsletter_AddForm
from . Article_add_form import ArticleForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from helpers.mailchimp_helper import Mailchimp_Helper

articles_added=[]

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
            subject = request.form['subject']
            my_data = AddNewsletter(subject,0,0)
            db.session.add(my_data)
            db.session.commit()
            flash(f'Form submitted successfully', 'success')
            newsletterId = db.session.query(AddNewsletter).order_by(AddNewsletter.newsletter_id.desc()).first()
            print("newsletter primary key", newsletterId)
            return redirect(url_for("Add_articles"))
    return render_template('add_newsletter.html',form=form)

@app.route("/add-articles",methods=["GET","POST"])
def Add_articles():
    "This page contains the form where user can add articles"
    url_data = ""
    form = ArticleForm()

    for url in articles_added:
        url_data += str(url) + "\n"
        form.added_articles.data = url_data
        
    
    if form.validate_on_submit():

        if form.add_more.data:
            category = form.category_id.data.category_id
            article_id = form.url.data
            title = form.title.data
            if form.category_id.data=="Select Category":
                flash(f'Please select category')
                return redirect(url_for("Add_articles"))
            else:
                #To be replaced by database
                file1 = open("replica_db.txt", "a")
                file1.write("%s\t%sn"%(category,article_id))
                file1.close()

                articles_added.append(title)
                return redirect(url_for("Add_articles"))

        if form.schedule.data:
            subject = form.subject.data
            opener= form.opener.data
            preview_text = form.preview_text.data
            
            if subject:                
                if opener:
                    if preview_text:
                        """
                        #if form.schedule.data:
                        content_data = NewsletterContent(1,category,url,0)
                        db.session.add(content_data)
                        db.session.commit()
                        """

                        #To be replace by database
                        file1 = open("replica_db1.txt", "a")  # append mode
                        file1.write("\t%s\t%s\n"%(opener,preview_text))
                        file1.close()

                        flash(f'Form submitted successfully', 'success')
                        articles_added.clear()
                        client = Mailchimp_Helper()
                        client.create_campaign(title,subject_line,preview_text)
                        return redirect(url_for("schedule"))
                    else:
                        flash(f'Enter preview text')

                else:
                    flash(f'Please enter the opener')
            else:
                    flash(f'Please enter the Subject')

        if form.cancel.data:
            flash(f'Clear all Fields!! Now select the articles')
            articles_added.clear()
            return redirect(url_for("Add_articles"))
            
            

    return render_template('add_article.html',form=form)


@app.route("/url/<category_id>")
def url(category_id):
    "This page fetches url based on category selected"

    url = Articles.query.filter_by(category_id=category_id).all()
    urlArray = []
    for each_element in url:
        urlobj ={}
        urlobj['article_id']= each_element.article_id
        urlobj['url']= each_element.url
        urlArray.append(urlobj)

    return jsonify({'url':urlArray})

@app.route("/description/<article_id>")
def description(article_id):
    "This page fetches the article description based on url selected"

    description = Articles.query.filter_by(article_id=article_id)

    descriptionArray = []
    for each_element in description:
        desc_obj ={}
        desc_obj['description']= each_element.description
        descriptionArray.append(desc_obj)

    return jsonify(descriptionArray[0]['description'])

@app.route("/readingtime/<article_id>")
def reading_time(article_id):
    "This article fetched reading time based on url selected"

    reading_time = Articles.query.filter_by(article_id=article_id).all()

    readingArray = []
    for each_element in reading_time:
        read_obj ={}
        read_obj['reading_time']= each_element.time
        readingArray.append(read_obj)

    return jsonify(readingArray[0]['reading_time'])

@app.route("/title/<article_id>")
def title(article_id):
    "This article fetched reading time based on url selected"

    title = Articles.query.filter_by(article_id=article_id).all()

    TitleArray = []
    for each_element in title:
        title_obj ={}
        title_obj['title']= each_element.title
        TitleArray.append(title_obj)


    return jsonify(TitleArray[0]['title'])
