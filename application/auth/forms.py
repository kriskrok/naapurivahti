from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class LoginForm(FlaskForm):
	username = StringField('Tunnus')
	password = PasswordField('Salasana')

	class Meta:
		csrf = False