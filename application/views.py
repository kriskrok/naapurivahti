from flask import render_template
from flask_login import current_user
from application import app

@app.route('/')
def index():
	message = 'Tervetuloa'
	if current_user.is_authenticated:
		message = 'Tervetuloa {}!'.format(current_user.username)
	return render_template('index.html', message = message)