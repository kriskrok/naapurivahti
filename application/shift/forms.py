from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import (Length, Required)
from wtforms.fields.html5 import DateField, TimeField


class ShiftForm(FlaskForm):
    comment = StringField('Ohjeita ja varustus', [Length(min=2)])
    date = DateField('Pvm', [Required()], format = '%Y-%m-%d')
    start_time = TimeField('Aloitus', [Required()] ,format = '%H:%M')
    end_time = TimeField('Lopetus', [Required()], format = '%H:%M')

    class Meta:
        csrf = False