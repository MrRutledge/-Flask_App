
# Importing the app package using app
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
     user = {'user': 'MrRutledge'}
     posts = [
        {
            'author': {'username': 'MrRutledge'},
            'body': 'Beautiful day in Croydon'
        },
        {
             'author':{'username':'MowHawk'},
             'body': 'The Titanic movie was so super'
        }
     ]
     return render_template('index.html',title='Brome', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
