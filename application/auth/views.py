from flask import render_template, request, redirect, url_for

from application import app
from application.auth.models import Account
from application.auth.forms import LoginForm

@app.route('/profile')
def profile():
	return render_template('profile.html')

#leaving methods undefined likely defaults exclusively to GET
@app.route('/login')
def open_loginform():
	form = LoginForm()

	return render_template('login_form.html', loginform = form)

@app.route('/login', methods = ['POST'])
def authenticate_login():
	form = LoginForm(request.form)
	# mahdolliset validoinnit
	print('Tiedot ', request.form, request.form['username'])

	user = Account.query.filter_by(username=form.username.data, password=form.password.data).first()
	if not user:
		return render_template('login_form.html', loginform = form,
								error = 'Invalid credentials')


	print("Käyttäjä " + user.username + " tunnistettiin")
	return redirect( url_for('index') )