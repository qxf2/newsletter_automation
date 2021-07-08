#Endpoints to different Pages/Endpoints
from operator import countOf
import re
from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from . models import Articles, db, Article_category, AddNewsletter, NewsletterContent,Newsletter_campaign
from . forms import AddArticlesForm
from newsletter import app
from . Article_add_form import ArticleForm
#from . Addpreview_form import Addpreviewform
import  json
from  helpers import mailchimp_helper


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

    content_json = []
    for each_element in result:
        contobj = {}
        contobj['newsletter_id']=each_element.newsletter_id
        contobj['title'] = each_element.title
        contobj['subject'] = each_element.subject
        contobj['opener'] = each_element.opener
        contobj["category name"] = each_element.category_name
        contobj["url"] = each_element.url
        content_json.append(contobj)
    #add_campaign(content_json)

    #writing the changes to campaign.json and returning the value
    jsonfile = 'campaign.json'
    with open (jsonfile, "w") as filehandler1:
        json.dump(content_json, filehandler1, indent=2)

        #open json file for reading
        filehandler2 = open(jsonfile)
        return filehandler2.read()

    #jsonfile.close('campaign.json')




def add_campaign(jsonfile):

   fil11 = json.dumps(jsonfile)
   #print(fil1)
   #campaign_content = '{"title":"title1","subject_line":"sub","preview_text":"preview texttt"}'
   fil1 = json.loads(fil11)
   print(fil1)
   #for i in fil1:
   #    print(type(i))
   title=""
   subject_line=""
   preview_text=""
   newsletter_id = 12
   for i in fil1:
       for k,v in i.items():
           #print(k)
           if k=="title":
              title=v
           elif k=="subject_line":
              subject_line=v
           elif k=="preview_text":
              preview_text=v
   campaign_id = mailchimp_helper.Mailchimp_Helper.create_campaign(title, subject_line, preview_text,preview_text)
   print(campaign_id)
   newletter_content_object = Newsletter_campaign(campaign_id==campaign_id,newsletter_id==12)
   db.session.add(newletter_content_object)
   db.session.commit()

   newsletterjson='{"in_this_issue":"inthis issue: test","comic":"category_name","comic_url":"url of comic","comic_text":"title of comic"}'
   newsletter_json = json.loads(newsletterjson)
   mailchimp_helper.Mailchimp_Helper.set_campaign_content(newsletter_json)


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
