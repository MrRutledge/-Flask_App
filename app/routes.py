from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rutledge'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Kim2'},
            'body': 'The average movie goer will!'
        }
    ]
    return render_template('index.html', title='Home2', user=user, posts=posts)
 
@app.route('/login')
def login():

    form = LoginForm()
    
    return render_template('login.html', title='Sign In', form=form)