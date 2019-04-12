
# Importing the app package using app
from flask import render_template, request,flash, redirect, url_for
from app import app, db
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
     # user = {'user': 'MrRutledge'}
      posts = [
        {
             'author': {'username': 'MrRutledge'},
             'body': 'Beautiful day in Jamaica'
         },
        {
             'author':{'username':'MowHawk'},
             'body': 'The Titanic movie was so super'
        }
     ]
      return render_template('index.html',title='Home ', posts=posts)

# login function
# Get and Post requests to the database 
"""
Login function 
     if the user is authenticated it 
          returns the index page 
     Otherwise We enter our details in the login form 
     if the details entered are valid 
     we can proceed 
     otherwise we have to resubmit 
"""  
@app.route('/login', methods=['GET', 'POST'])
def login():
     if current_user.is_authenticated:
          return redirect(url_for('index'))
     form = LoginForm()
     if form.validate_on_submit():
         user = User.query.filter_by(username=form.username.data).first()
         if user is None or not user.check_password(form.password.data):
            flash('Invalid details: Check and resubmit')
            return redirect(url_for('login'))
         login_user(user, remember=form.remember_me.data)
         next_page = request.args.get('next')
         if not next_page or url_parse(next_page).netloc != '':
              next_page = url_for('index')
         return redirect(next_page)
     return render_template('login.html', title='Sign In', form=form)

#function for logout 
@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('index'))

# function to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required

def user(username):
     user = User.query.filter_by(username=username).first_or_404()
     posts = [
          {'author': user, 'body':'Test post #1'},
          {'author': user, 'body': 'Test post #2'}
     ]
     return render_template('user_html', user=user, posts=posts)