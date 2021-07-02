#Endpoints to different Pages/Endpoints
from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from . models import Articles, db, Article_category, AddNewsletter, NewsletterContent
from . forms import AddArticlesForm
from newsletter import app
from . Article_add_form import ArticleForm

articles_added=[]
article_id_list=[]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/articles', methods=['GET', 'POST'])
def articles():
    "This page adds articles to the database"
    addarticlesform = AddArticlesForm(request.form)
    category = AddArticlesForm(request.form)
    if category.validate_on_submit():
        return '<html><h1>{}</h1></html>'.format(category.category_name.data.category_id)
    if request.method == 'POST':
        article = Articles(addarticlesform.url.data,addarticlesform.title.data,addarticlesform.description.data, addarticlesform.time.data, addarticlesform.category_id.data.category_id)
        db.session.add(article)
        db.session.commit()
        msg = "Record added Successfully"
        return render_template('result.html', msg=msg)

    return render_template('articles.html',addarticlesform=addarticlesform, category=category)

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
                flash('Please select category')
                return redirect(url_for("Add_articles"))
            else:
                article_id_list.append(article_id)
                articles_added.append(title)
                return redirect(url_for("Add_articles"))

        if form.schedule.data:
            subject = form.subject.data
            opener= form.opener.data
            preview_text = form.preview_text.data

            if subject:
                if opener:
                    if preview_text:
                        add_newsletter_object=AddNewsletter(subject=subject,opener=opener,preview=preview_text)
                        db.session.add(add_newsletter_object)
                        db.session.flush()
                        newsletter_id = add_newsletter_object.newsletter_id
                        db.session.commit()
                        for each_article in article_id_list:
                            newletter_content_object = NewsletterContent(article_id=each_article,newsletter_id=newsletter_id)
                            db.session.add(newletter_content_object)
                            db.session.flush()
                            newsletter_content_id = newletter_content_object.newsletter_content_id
                            db.session.commit()

                        flash('Form submitted successfully ')
                        articles_added.clear()
                        article_id_list.clear()
                        return redirect(url_for("Add_articles"))
                    else:
                        flash('Enter preview text')

                else:
                    flash('Please enter the opener')
            else:
                    flash('Please enter the Subject')

        if form.cancel.data:
            flash('Clear all Fields!! Now select the articles')
            articles_added.clear()
            article_id_list.clear()
            return redirect(url_for("Add_articles"))

    all_articles = [Articles.query.filter_by(article_id=article_id).one() for article_id in article_id_list]

    return render_template('add_article.html',form=form, all_articles=all_articles,article_list=article_id_list)


@app.route("/url/<category_id>")
def url(category_id):
    "This method fetches url and article_id based on category selected"

    url = Articles.query.filter_by(category_id=category_id).all()
    urlArray = []
    for each_element in url:
        urlobj ={}
        if each_element.newsletter_id == None:
            urlobj['article_id']= each_element.article_id
            urlobj['url']= each_element.url
            urlArray.append(urlobj)

    return jsonify({'url':urlArray})


@app.route("/description/<article_id>")
def description(article_id):
    "This method fetches the article description based on article selected"

    description = Articles.query.filter_by(article_id=article_id)
    descriptionArray = []
    for each_element in description:
        desc_obj ={}
        desc_obj['description']= each_element.description
        descriptionArray.append(desc_obj)

    return jsonify(descriptionArray[0]['description'])


@app.route("/readingtime/<article_id>")
def reading_time(article_id):
    "This method fetched reading time based on article selected"

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

@app.route('/view-articles')
def view_articles():
    addarticlesform = AddArticlesForm(request.form)
    article_data = Articles.query.all()
    return render_template('view_articles.html', addarticlesform=addarticlesform,article_data=article_data)



