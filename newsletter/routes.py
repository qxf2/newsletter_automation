from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template


from . forms import AddArticlesForm
from . models import articles, db
from flask import render_template
from newsletter import app


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/articles', methods = ['GET', 'POST'])
def articles():
   if request.method == 'POST':
      if not request.form['url'] or not request.form['title'] or not request.form['description'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         article = Articles(request.form['url'], request.form['title'], request.form['description'], request.form['time'])

         db.session.add(member)
         db.session.commit()
         flash('Record was successfully added')
   return render_template('articles.html')


if __name__ == '__main__':
    app.run()
