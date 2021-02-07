from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField, TimeField


class ShiftForm(FlaskForm):
    comment = StringField('Ohjeita ja varustus')
    date = DateField('Pvm', format = '%Y-%m-%d')
    start_time = TimeField('Aloitus', format = '%H:%M')
    end_time = TimeField('Lopetus', format = '%H:%M')

    class Meta:
        csrf = False