from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Length, Required
from wtforms.fields.html5 import TimeField

class CreateObservationForm(FlaskForm):
    comment = TextAreaField('Kuvaus', validators=[Required(), Length(min=3, max=600, message='Kuvauksen oltava vähintään 3 merkkiä pitkä')])
    timing = TimeField('Havaintoaika', [Required()] ,format = '%H:%M')
    requires_action = BooleanField('Vaatii jatkotoimenpiteitä')

    class Meta:
        csrf = False