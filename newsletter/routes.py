from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template

from . models import Articles, db, Article_category
from . forms import AddArticlesForm
#from . models import Articles, db
from flask import render_template
from newsletter import app


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/articles', methods=['GET', 'POST'])
def articles():
        
        addarticlesform = AddArticlesForm(request.form)
        category = addarticlesform = AddArticlesForm(request.form)
        category.category_id.choices = [(Article_category.category_id, Article_category.category_name) for article_category in Article_category.query.all()]
        if request.method == 'POST':
#            addarticleform = AddArticlesForm(request.form)
            article = Articles(addarticlesform.url.data,addarticlesform.title.data,addarticlesform.description.data, addarticlesform.time.data, addarticlesform.category_id.data)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('articles'))
        return render_template('articles.html',addarticlesform=addarticlesform, category=category)


if __name__ == '__main__':
    app.run(debug=True)
