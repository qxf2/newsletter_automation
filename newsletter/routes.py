#Endpoints to different Pages/Endpoints
from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from sqlalchemy.orm import query
from . models import Articles, db, Article_category, AddNewsletter, NewsletterContent
from . forms import AddArticlesForm
from newsletter import app
from . create_newsletter_form import ArticleForm
from . edit_article_form import EditArticlesForm

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


def add_articles_to_newsletter(subject, opener, preview_text):
    "Adding articles to newsletter"
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
        articles_newsletter_id = Articles.query.filter(Articles.article_id==each_article).update({"newsletter_id":newsletter_id})
        db.session.commit()

        flash('Form submitted successfully ')
        articles_added.clear()
        article_id_list.clear()

    return article_id_list


@app.route("/create-newsletter",methods=["GET","POST"])
def add_articles():
    "This page contains the form where user can add articles"
    form = ArticleForm()
    url_data = ",".join(articles_added)
    category = form.category_id.data
    article_id = form.url.data
    title = form.title.data
    subject = form.subject.data
    opener= form.opener.data
    preview_text = form.preview_text.data

    if form.validate_on_submit():
        if form.add_more.data:
            if form.category_id.data is None:
                flash('Please select Category','danger')
                return redirect(url_for("add_articles"))
            if article_id=="Select URL":
                flash('Please select URL','danger')
                return redirect(url_for("add_articles"))
            else:
                if article_id not in article_id_list:
                    article_id_list.append(article_id)
                    articles_added.append(title)
                    return redirect(url_for("add_articles"))
                else:
                    flash('Already selected !! Please select another article ', 'danger')
                    return redirect(url_for("add_articles"))

        if form.schedule.data:
            if subject and opener and preview_text and article_id_list:
                add_articles_to_newsletter(subject, opener, preview_text)
                return redirect(url_for("add_articles"))

            else:
                flash('Please check have you selected the articles, filled the subject, opener or preview text')

        if form.cancel.data:
            flash('Clear all Fields!! Now select the articles', 'info')
            articles_added.clear()
            article_id_list.clear()
            return redirect(url_for("add_articles"))

    all_articles = [Articles.query.filter_by(article_id=article_id).one() for article_id in article_id_list]

    return render_template('create_newsletter.html',form=form, all_articles=all_articles,article_list=article_id_list)


@app.route("/url/<category_id>")
def url(category_id):
    "This method fetches url and article_id based on category selected"

    url = Articles.query.filter_by(category_id=category_id).all()
    url_array = []
    for each_element in url:
        url_obj ={}
        if each_element.newsletter_id == None:
            url_obj['article_id']= each_element.article_id
            url_obj['url']= each_element.url
            url_array.append(url_obj)

    return jsonify({'url':url_array})


@app.route("/description/<article_id>")
def description(article_id):
    "This method fetches the article description based on article selected"

    description = Articles.query.filter_by(article_id=article_id)
    description_array = []
    for each_element in description:
        desc_obj ={}
        desc_obj['description']= each_element.description
        description_array.append(desc_obj)

    return jsonify(description_array[0]['description'])


@app.route("/readingtime/<article_id>")
def reading_time(article_id):
    "This method fetched reading time based on article selected"

    reading_time = Articles.query.filter_by(article_id=article_id).all()

    reading_array = []
    for each_element in reading_time:
        read_obj ={}
        read_obj['reading_time']= each_element.time
        reading_array.append(read_obj)

    return jsonify(reading_array[0]['reading_time'])


@app.route("/title/<article_id>")
def title(article_id):
    "This article fetched reading time based on url selected"

    title = Articles.query.filter_by(article_id=article_id).all()
    Title_array = []
    for each_element in title:
        title_obj ={}
        title_obj['title']= each_element.title
        Title_array.append(title_obj)

    return jsonify(Title_array[0]['title'])

@app.route('/manage-articles')
def manage_articles():
    add_articles_form = AddArticlesForm(request.form)
    article_data = Articles.query.all()
    return render_template('manage_articles.html', addarticlesform=add_articles_form,article_data=article_data)


@app.route("/edit/<article_id>",methods=["GET","POST"])
def update_article(article_id):
    "This method is used to edit articles based on article_id"

    article = Articles.query.filter_by(article_id=article_id).all()
    for each_article in article:
        form = EditArticlesForm(title=each_article.title,
                            url=each_article.url,
                            description=each_article.description,
                            time=each_article.time,
                            category_id=each_article.category_id)

    if form.validate_on_submit():
        edited_title=form.title.data
        edited_url=form.url.data
        edited_description=form.description.data
        edited_time=form.time.data
        edited_category= int(form.category_id.data)
        Articles.query.filter(Articles.article_id==article_id).update({"title":edited_title,"url":edited_url,"description":edited_description,"time":edited_time,"category_id":edited_category})

        db.session.commit()
        return redirect(url_for("manage_articles"))

    return render_template('edit_article.html',form=form)


@app.route("/delete/<article_id>", methods=["GET","POST"])
def delete_article(article_id):
    "Deletes an article"
    articles_delete = Articles.query.filter_by(article_id=article_id).value(Articles.newsletter_id)

    if articles_delete is not None:
        flash('Cannot delete!! Article is already a part of campaign')
    else:
        delete_article = Articles.query.get(article_id)
        db.session.delete(delete_article)
        db.session.commit()

    return redirect(url_for("manage_articles"))


@app.route("/removearticle",methods=["GET","POST"])
def remove_article():
    "Remove article from the list"
    form = ArticleForm()
    article_id = request.form.get('articleid')
    article_id_list.remove(article_id)

    return render_template('create_newsletter.html',form=form,article_list=article_id_list)
