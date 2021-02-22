from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.shift.models import Guardshift
from application.shift.forms import ShiftForm
from application.report.models import Report

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
    new_shift = Guardshift(comment, date, start, end)

    db.session().add(new_shift)
    db.session().commit()

    #automagically conjure a blank report upon shift creation
    report = Report(new_shift.shift_id, current_user.user_id)
    db.session().add(report)
    db.session().commit()

    return redirect( url_for('list_shifts') )