from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from newsletter import app
from . models import AddNewsletter, db, Article_category, Articles
from . Newsletter_add_form import Newsletter_AddForm
from . Article_add_form import ArticleForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
<<<<<<< HEAD
=======
from helpers.mailchimp_helper import Mailchimp_Helper
>>>>>>> newsletter_forms_team2

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
<<<<<<< HEAD
    form = ArticleForm(request.form)
      
    for url in articles_added:
        url_data += str(url) + "\n"
        form.added_articles.data = url_data
    #if request.method == 'POST':
        
    if form.validate_on_submit():
        category=form.category_id.data.category_id
        url= form.url.data.article_id
        description=form.description.data
        reading_time=form.reading_time.data
        title = form.title.data
        opener= form.opener.data
        preview_text = form.preview_text.data
        

=======
    form = ArticleForm()
    # category = ArticleForm(request.form)
    # url = ArticleForm(request.form)
    # if category.validate_on_submit():
    #         return '<html><h1>{}</h1></html>'.format(category.category_name.data.category_id)   
    for url in articles_added:
        url_data += str(url) + "\n"
        form.added_articles.data = url_data
        
    if form.validate_on_submit():
        category = form.category_id.data
        article_url = form.url.data.article_id
        # description=form.description.data
        # reading_time=form.reading_time.data
        # title = form.title.data
        opener= form.opener.data
        preview_text = form.preview_text.data
>>>>>>> newsletter_forms_team2
        if form.add_more.data:
            if form.category.data=="Select Category":
                flash(f'Please select category')
                return redirect(url_for("Add_articles"))
            else:
<<<<<<< HEAD
                #To be replaced by database
                file1 = open("replica_db.txt", "a")
                file1.write("%s\t%s\t%s\t%s\t%s\n"%(category,url,title,description,reading_time))
                file1.close()

                articles_added.append(description)
                return redirect(url_for("Add_articles"))

        #if form.schedule.data:
        content_data = NewsletterContent(1,category,url,0)
        db.session.add(content_data)
        db.session.commit()
            
        """
=======
                print(form)
                print(category)
                my_data = NewsletterContent(newsletterId,category,article_url,0)
                db.session.add(my_data)
                db.session.commit()
                #To be replaced by database
                file1 = open("replica_db.txt", "a")
                file1.write("%s\t%s\t%s\t%s\t%s\n"%(category,article_url,title,description,reading_time))
                file1.close()
                articles_added.append(url)
                return redirect(url_for("Add_articles"))

        if form.schedule.data:
>>>>>>> newsletter_forms_team2
            if opener:
                if preview_text:
                    #To be replace by database
                    file1 = open("replica_db1.txt", "a")  # append mode
                    file1.write("\t%s\t%s\n"%(opener,preview_text))
                    file1.close()

                    flash(f'Form submitted successfully', 'success')
                    articles_added.clear()
<<<<<<< HEAD
                    return redirect(url_for("index"))
=======
                    client = Mailchimp_Helper()
                    client.create_campaign(title,subject_line,preview_text)
                    return redirect(url_for("schedule"))
>>>>>>> newsletter_forms_team2
                else:
                    flash(f'Enter preview text')

            else:
                flash(f'Please enter the opener')
<<<<<<< HEAD
        """   
                
=======
>>>>>>> newsletter_forms_team2
    return render_template('add_article.html',form=form)  


@app.route("/url/<category_id>")
def url(category_id):
    "This page fetches url based on category selected"
<<<<<<< HEAD
    
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
=======
>>>>>>> newsletter_forms_team2
    
    url = Articles.query.filter_by(category_id=category_id).all()
    urlArray = []
    for each_element in url:
        urlobj ={}
        urlobj['article_id']= each_element.article_id
        urlobj['url']= each_element.url
        urlArray.append(urlobj)
        
    return jsonify({'url':urlArray})

@app.route("/description/<url>")
def description(url):
    "This page fetches the article description based on url selected"

    #Data to be replaced from DB
    if url=="comic_url1":
        description = ""
    if url=="comic_url2":
        description = ""
    if url=="thisweek_url1":
        description = "this week article 1"
    if url=="thisweek_url2":
        description = "this week article 2"
    if url=="past_url1":
        description = "past week article 2"
    if url=="past_url2":
        description = "past week article 2"

    return jsonify(description)

@app.route("/readingtime/<url>")
def reading_time(url):
    "This article fetched reading time based on url selected"

    #Data to be replace from DB
    if url=="comic_url1":
        reading_time = ""
    if url=="comic_url2":
        reading_time = ""
    if url=="thisweek_url1":
        reading_time = "10 mins"
    if url=="thisweek_url2":
        reading_time = "20 mins"
    if url=="past_url1":
        reading_time = "30 mins"
    if url=="past_url2":
        reading_time = "40 mins"

    return jsonify(reading_time)

@app.route("/title/<url>")
def title(url):
    "This article fetched reading time based on url selected"

    #Data to be replace from DB
    if url=="comic_url1":
        title = "Comic 1"
    if url=="comic_url2":
        title = "Comic 2"
    if url=="thisweek_url1":
        title = "This week Article 1"
    if url=="thisweek_url2":
        title = "This week Article 2"
    if url=="past_url1":
        title = "Past week Article 1"
    if url=="past_url2":
        title = "Past week Article 2"

<<<<<<< HEAD
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
=======
    return jsonify(title)
>>>>>>> newsletter_forms_team2

if __name__ == '__main__':
    app.run(debug=True)
