from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user
from flask_login.utils import login_required, logout_user

from datetime import datetime

from application import app, db
from application.auth.models import Account
from application.auth.forms import LoginForm, CreateUserForm

@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html')

@app.route('/signup')
def open_signupform():
	return render_template('signup_form.html', userform = CreateUserForm())

@app.route('/signup', methods = ['POST'])
def authenticate_signup():
	form = CreateUserForm(request.form)

	if not form.validate():
		return render_template('signup_form.html', userform = form)

	email_taken = Account.query.filter_by(email=form.email.data).first()
	if email_taken:
		return render_template('signup_form.html', userform = form, error = 'Syötä toinen spostiosoite')

	username_taken = Account.query.filter_by(username=form.username.data).first()
	if username_taken:
		return render_template('signup_form.html', userform = form, error = 'Valitse toinen tunnus')

	new_account = Account(email=form.email.data, username=form.username.data)

	new_account.set_password(form.password.data)
	
	db.session.add(new_account)
	db.session.commit()
	login_user(new_account)
	return redirect( url_for('index') )


@app.route('/login')
def open_loginform():
	form = LoginForm()

	return render_template('login_form.html', loginform = form)

@app.route('/login', methods = ['POST'])
def authenticate_login():
	if current_user.is_authenticated:
		return redirect( url_for('index') )

	form = LoginForm(request.form)
	if not form.validate():
		return render_template('login_form.html', loginform = form)

	user = Account.query.filter_by(username=form.username.data).first()
	
	if user and user.check_password(password=form.password.data):
		login_user(user)

		# update last_login
		user.last_login = datetime.now()
		db.session.commit()
		return redirect( url_for('index') )

	return render_template('login_form.html', loginform = form,
							error = 'Virheellinen syöte')


@app.route('/logout')
def authenticate_logout():
	logout_user()
	return redirect( url_for('index') )