from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from newsletter import app
from . models import AddNewsletter, db, Article_category, Articles
from . Newsletter_add_form import Newsletter_AddForm
from . Article_add_form import ArticleForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField

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
            return redirect(url_for("Add_articles"))
    return render_template('add_newsletter.html',form=form)

@app.route("/add-articles",methods=["GET","POST"])
def Add_articles():
    "This page contains the form where user can add articles"
    url_data = ""
    form = ArticleForm(request.form)
    category = ArticleForm(request.form)
    url = ArticleForm(request.form)
    if category.validate_on_submit():
            return '<html><h1>{}</h1></html>'.format(category.category_name.data.category_id)
    
        
    for url in articles_added:
        url_data += str(url) + "\n"
        form.added_articles.data = url_data
    if request.method == 'POST':
        
        if form.validate_on_submit():
            category=form.category_id.data.category_id
            url= form.url.data
            description=form.description.data
            reading_time=form.reading_time.data
            title = form.title.data
            opener= form.opener.data
            preview_text = form.preview_text.data

            if form.add_more.data:
                if form.category.data=="Select Category":
                    flash(f'Please select category')
                    return redirect(url_for("Add_articles"))
                else:
                    #To be replaced by database
                    file1 = open("replica_db.txt", "a")
                    file1.write("%s\t%s\t%s\t%s\t%s\n"%(category,url,title,description,reading_time))
                    file1.close()

                    articles_added.append(url)
                    return redirect(url_for("Add_articles"))

            if form.schedule.data:
                if opener:
                    if preview_text:
                        #To be replace by database
                        file1 = open("replica_db1.txt", "a")  # append mode
                        file1.write("\t%s\t%s\n"%(opener,preview_text))
                        file1.close()

                        flash(f'Form submitted successfully', 'success')
                        articles_added.clear()
                        return redirect(url_for("index"))
                    else:
                        flash(f'Enter preview text')

                else:
                    flash(f'Please enter the opener')
    return render_template('add_article.html',form=form, category=category)  
    

@app.route("/url/<category_id>")
def url(category_id):
    "This page fetches url based on category selected"
    
    url = Articles.query.filter_by(category_id=category_id).all()
    urlArray = []
    for each_element in url:
        print(each_element)
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

    return jsonify(title)

if __name__ == '__main__':
    app.run(debug=True)
