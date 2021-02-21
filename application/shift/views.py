from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.shift.models import Guardshift
from application.shift.forms import ShiftForm

@app.route('/shifts/list')
@login_required
def list_shifts():
	return render_template('shifts_list.html', shifts = Guardshift.query.all())

@app.route('/shifts/new/shift')
@login_required
def open_shiftform():
    form = ShiftForm()

    return render_template('shift_form.html', shiftform = form)

@app.route('/shifts/new/shift/', methods=['POST'])
@login_required
def shift_create():
    form = ShiftForm(request.form)
    comment = form.comment.data
    date = form.date.data
    start = form.start_time.data
    end = form.end_time.data
    shift = Guardshift(comment, date, start, end)

    db.session().add(shift)
    db.session().commit()

    return redirect( url_for('list_shifts') )