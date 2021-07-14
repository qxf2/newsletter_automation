#Endpoints to different Pages/Endpoints
import  json
import re
from operator import countOf
from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from . models import Articles, db, Article_category, AddNewsletter, NewsletterContent,Newsletter_campaign
from . forms import AddArticlesForm
from newsletter import app
from . Article_add_form import ArticleForm
from  helpers import mailchimp_helper
import datetime

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

        if form.preview_newsletter.data:
            subject = form.subject.data
            opener= form.opener.data

            if subject:
                if opener:
                    add_newsletter_object=AddNewsletter(subject=subject,opener=opener)
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
                    return redirect(url_for("previewnewsletter",newsletter_id=newsletter_id))
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

@app.route("/preview_newsletter/<newsletter_id>",methods=["GET","POST"])
def previewnewsletter(newsletter_id):
    "To populate the preview newsletter page"
    content =  AddNewsletter.query.with_entities(AddNewsletter.newsletter_id,AddNewsletter.subject,AddNewsletter.opener,Article_category.category_name,Articles.title,Articles.url,Articles.description,Articles.time).filter(AddNewsletter.newsletter_id == newsletter_id).join(NewsletterContent, NewsletterContent.newsletter_id==AddNewsletter.newsletter_id).join(Articles, Articles.article_id==NewsletterContent.article_id).join(Article_category, Article_category.category_id == Articles.category_id)

    return render_template('preview_newsletter.html',content=content)

@app.route("/create_campaign",methods=["GET","POST"])
def create_campaign():
    """
    create the campaign and return the campaign id
    update campaign table with this id
    create the newsletter_json needed for mailchimp api
    call mailchimp content setting api
    """
    newsletter_id_db = db.session.query(NewsletterContent.newsletter_id).order_by(NewsletterContent.newsletter_id.desc()).first()
    for row in newsletter_id_db:
        newsletter_id= row
    content =  AddNewsletter.query.with_entities(AddNewsletter.newsletter_id,AddNewsletter.subject,AddNewsletter.opener,
    Article_category.category_name,Articles.title,Articles.url,Articles.description,Articles.time).join(NewsletterContent, NewsletterContent.newsletter_id==AddNewsletter.newsletter_id).filter_by(newsletter_id=newsletter_id).join(Articles, Articles.article_id==NewsletterContent.article_id).join(Article_category, Article_category.category_id == Articles.category_id)

    result = db.session.execute(content)

    newsletter = {'title': '', 'in_this_issue': '', 'comic': {'comic_url': '', 'comic_text': ''},
    'this_week_articles': [],
    'past_articles':[],
    'automation_corner':[]}
    newsletter_json = []
    for each_element in result:
        newsletter['title']= "The Informed Tester’s Newsletter:" + datetime.date.today().strftime('%d-%B-%Y')
        newsletter['in_this_issue'] = "In this issue "+ each_element.opener
        if each_element.category_name == 'comic':
            newsletter['comic']['comic_url']=each_element.url
            newsletter['comic']['comic_text']= "This is a comic"
        if each_element.category_name == 'currentweek':
            newsletter['this_week_articles'].append({'title':each_element['title'], 'url':each_element['url'], 'description':each_element['description'],'reading_time':each_element['time']})
        if each_element.category_name == 'pastweek':
            newsletter['past_articles'].append({'title':each_element['title'], 'url':each_element['url'], 'description':each_element['description'],'reading_time':each_element['time']})
        if each_element.category_name == 'automation corner':
            newsletter['automation_corner'].append({'title':each_element['title'], 'url':each_element['url'], 'description':each_element['description'],'reading_time':each_element['time']})

    add_campaign(newsletter,newsletter_id)
    #newsletter_json.append(newsletter)
    jsonfile = 'newsletter.json'
    with open(jsonfile, "w") as flw:
        json.dump(newsletter, flw, indent=4)

        flr = open(jsonfile)
        return flr.read()

    return(newsletter)


def add_campaign(newsletter,newsletter_id):

    campaign_name=newsletter['title']
    subject=newsletter['title'] 
    preview_text="preview new1"

    #creating campaign here
    clientobj = mailchimp_helper.Mailchimp_Helper()
    #print("title,subject,preview",title,subject,preview_text)
    clientobj.create_campaign(campaign_name,subject,preview_text)
    campaign_id = clientobj.campaign_id

    newletter_content_object = Newsletter_campaign(campaign_id=campaign_id,newsletter_id=newsletter_id)
    db.session.add(newletter_content_object)
    db.session.commit()


    contentobj = mailchimp_helper.Mailchimp_Helper()
    contentobj.set_campaign_content(newsletter,campaign_id)

@app.route("/url/<category_id>")
def url(category_id):
    "This method fetches url and article_id based on category selected"

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
