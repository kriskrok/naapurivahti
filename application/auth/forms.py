from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import DateField, TimeField

class LoginForm(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')

	class Meta:
		csrf = False


#class ShiftForm(FlaskForm):
#    comment = StringField('Ohjeita ja varustus')
#    date = DateField('Pvm', format = '%Y-%m-%d')
#    start_time = TimeField('Aloitus', format = '%H:%M')
#    end_time = TimeField('Lopetus', format = '%H:%M')
#
#    class Meta:
#        csrf = False