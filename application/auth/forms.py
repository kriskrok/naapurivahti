from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Length, Regexp, Required


class LoginForm(FlaskForm):
	username = StringField('Tunnus', validators=[Required(), Length(min=3, max=40, message='Tunnuksen tulee olla vähintään 3 ja enintään 40 merkkiä pitkä')])
	password = PasswordField('Salasana', validators=[Required()])

	class Meta:
		csrf = False

class CreateUserForm(FlaskForm):
	username = StringField('Tunnus', validators=[Required(), Length(min=3, max=40, message='Tunnuksen tulee olla vähintään 3 ja enintään 40 merkkiä pitkä')])
	email = EmailField('Sposti', validators=[Required(), Regexp('^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$', message='Syöttämäsi sähköpostiosoite ei kelpaa')])
	password = PasswordField('Salasana', validators=[DataRequired(), Length(min=8, max=255, message='Salasanan on oltava vähintään 8 merkkiä pitkä')])
	confirm = PasswordField('Syötähän varoiksi uudemman kerran', validators=[DataRequired(), EqualTo('password', message='Salasanat eivät vastaa toisiaan')])

	class Meta:
		csrf = False
