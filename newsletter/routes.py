from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template


from . forms import AddArticlesForm
from . models import Articles, db
from flask import render_template
from newsletter import app


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/articles', methods=['GET', 'POST'])
def articles():
        addarticle = AddArticlesForm(request.form)
        if request.method == 'POST':
            addarticleform = AddArticlesForm(request.form)
            article = Articles(addarticleform.url.data,addarticleform.title.data,addarticleform.description.data)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('articles'))
        return render_template('articles.html')


if __name__ == '__main__':
    app.run(debug=True)
