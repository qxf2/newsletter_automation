#Endpoints to different Pages/Endpoints
import  json
import re
import requests
from operator import countOf
from builtins import Exception
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify,session
from sqlalchemy.orm.exc import MultipleResultsFound
from . models import Articles, db, Article_category, AddNewsletter, NewsletterContent,Newsletter_campaign
from . forms import AddArticlesForm
from newsletter import app
from  helpers import mailchimp_helper
import datetime
from sqlalchemy.orm import query
from . forms import AddArticlesForm
from . create_newsletter_form import ArticleForm
from . edit_article_form import EditArticlesForm
import newsletter.sso_google_oauth as sso
from helpers.authentication_required import Authentication_Required

articles_added=[]
article_id_list=[]


@app.route("/")
def home():
    "Login page for an app"
    return render_template('login.html')


@app.route("/login")
def login():
    "Login redirect"
    return redirect(sso.REQ_URI)


@app.route('/callback')
def callback():
    "Redirect after Google login & consent"

    # Get the code after authenticating from the URL
    code = request.args.get('code')

    # Generate URL to generate token
    token_url, headers, body = sso.CLIENT.prepare_token_request(
            sso.URL_DICT['token_gen'],
            authorisation_response=request.url,
            # request.base_url is same as DATA['redirect_uri']
            redirect_url=request.base_url,
            code=code)

    # Generate token to access Google API
    token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(sso.CLIENT_ID, sso.CLIENT_SECRET))

    # Parse the token response
    sso.CLIENT.parse_request_body_response(json.dumps(token_response.json()))

    # Add token to the  Google endpoint to get the user info
    # oauthlib uses the token parsed in the previous step
    uri, headers, body = sso.CLIENT.add_token(sso.URL_DICT['get_user_info'])

    # Get the user info
    response_user_info = requests.get(uri, headers=headers, data=body)
    info = response_user_info.json()
    user_info = info['email']
    user_email_domain = re.search("@[\w.]+",user_info).group()
    if user_email_domain == '@qxf2.com':
        session['logged_user'] = user_info
        return render_template('home.html')
    else:
        return render_template('unauthorized.html')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@app.route('/home')
@Authentication_Required.requires_auth
def index():
    return render_template('home.html')


@app.route('/articles', methods=['GET', 'POST'])
@Authentication_Required.requires_auth
def articles():
    "This page adds articles to the database"
    addarticlesform = AddArticlesForm(request.form)
    category = AddArticlesForm(request.form)
    if category.validate_on_submit():
        return '<html><h1>{}</h1></html>'.format(category.category_name.data.category_id)
    if request.method == 'POST':
        article = Articles(addarticlesform.url.data,addarticlesform.title.data,addarticlesform.description.data, addarticlesform.time.data, addarticlesform.category_id.data.category_id)
        db.session.add(article)
        try:
            if url == db.session.query(Articles).filter(Articles.url == addarticlesform.url.data).one_or_none():
                msg = ""
            else:
                db.session.commit()
                msg = "Record added Successfully"
        except MultipleResultsFound as e:
            msg = e
        #db.session.commit()
        #msg = "Record added Successfully"
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

    return article_id_list, newsletter_id


@app.route("/create-newsletter",methods=["GET","POST"])
@Authentication_Required.requires_auth
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

        if form.preview_text.data:
            if subject and opener and preview_text and article_id_list:
                article_list, newsletter_id = add_articles_to_newsletter(subject, opener, preview_text)
                return redirect(url_for("previewnewsletter",newsletter_id=newsletter_id))
                #return redirect(url_for("add_articles"))
            else:
                flash('Please check have you selected the articles, filled the subject, opener or preview text','danger')

        if form.cancel.data:
            flash('Clear all Fields!! Now select the articles', 'info')
            articles_added.clear()
            article_id_list.clear()
            return redirect(url_for("add_articles"))

    all_articles = [Articles.query.filter_by(article_id=article_id).one() for article_id in article_id_list]

    return render_template('create_newsletter.html',form=form, all_articles=all_articles,article_list=article_id_list)

@app.route("/preview_newsletter/<newsletter_id>",methods=["GET","POST"])
def previewnewsletter(newsletter_id):
    "To populate the preview newsletter page"
    content =  AddNewsletter.query.with_entities(AddNewsletter.newsletter_id,AddNewsletter.subject,AddNewsletter.opener,AddNewsletter.preview,Article_category.category_name,Articles.title,Articles.url,Articles.description,Articles.time).filter(AddNewsletter.newsletter_id == newsletter_id).join(NewsletterContent, NewsletterContent.newsletter_id==AddNewsletter.newsletter_id).join(Articles, Articles.article_id==NewsletterContent.article_id).join(Article_category, Article_category.category_id == Articles.category_id)

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
    content =  AddNewsletter.query.with_entities(AddNewsletter.newsletter_id,AddNewsletter.subject,AddNewsletter.opener,AddNewsletter.preview,Article_category.category_name,Articles.title,Articles.url,Articles.description,Articles.time).join(NewsletterContent, NewsletterContent.newsletter_id==AddNewsletter.newsletter_id).filter_by(newsletter_id=newsletter_id).join(Articles, Articles.article_id==NewsletterContent.article_id).join(Article_category, Article_category.category_id == Articles.category_id)

    result = db.session.execute(content)

    newsletter = {'title': '', 'in_this_issue': '','preview':'', 'comic': {'comic_url': '', 'comic_text': ''},
    'this_week_articles': [],
    'past_articles':[],
    'automation_corner':[]}
    newsletter_json = []
    for each_element in result:
        newsletter['title']= each_element.subject +" " + datetime.date.today().strftime('%d-%B-%Y')
        newsletter['in_this_issue'] = "In this issue "+ each_element.opener
        newsletter['preview']=each_element.preview
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
    preview_text=newsletter['preview']

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
@Authentication_Required.requires_auth

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
@Authentication_Required.requires_auth

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
@Authentication_Required.requires_auth

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
@Authentication_Required.requires_auth

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
@Authentication_Required.requires_auth

def manage_articles():
    add_articles_form = AddArticlesForm(request.form)
    article_data = Articles.query.all()
    return render_template('manage_articles.html', addarticlesform=add_articles_form,article_data=article_data)


@app.route("/edit/<article_id>",methods=["GET","POST"])
@Authentication_Required.requires_auth

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
@Authentication_Required.requires_auth

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
@Authentication_Required.requires_auth

def remove_article():
    "Remove article from the list"
    form = ArticleForm()
    article_id = request.form.get('articleid')
    article_id_list.remove(article_id)

    return render_template('create_newsletter.html',form=form,article_list=article_id_list)
