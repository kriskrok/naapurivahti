from datetime import date
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.shift.models import Guardshift
from application.shift.forms import ShiftForm
from application.report.models import Report

@app.route('/shifts/list')
@login_required
def list_shifts():
    return render_template('shifts_list.html', shifts = Guardshift.query.all(), suurmartta=current_user.is_suurmartta())

@app.route('/shifts/new/shift')
@login_required
def open_shiftform():
    if not current_user.is_suurmartta():
        redirect(url_for('list_shifts'))

    shift_id = request.args.get('shift_id')
    form = ShiftForm()

    if shift_id:
        guardshift = Guardshift.query.get(shift_id)
    
        form.comment.data = guardshift.comment
        form.date.data = guardshift.date
        form.start_time.data = guardshift.start_time
        form.end_time.data = guardshift.end_time

    return render_template('shift_form.html', shiftform = form, shift_id=shift_id)

@app.route('/shifts/new/shift/', methods=['POST'])
@login_required
def shift_create():
    if current_user.is_suurmartta():
        form = ShiftForm(request.form)

        shift_id = request.args.get('shift_id')

        if not form.validate():
            return render_template('shift_form.html', shiftform = form, shift_id=shift_id)

        if shift_id:
            new_shift = Guardshift.query.get(shift_id)
        else:
            new_shift = Guardshift(date=form.date.data, start=form.start_time.data, end=form.end_time.data)
            db.session().add(new_shift)

        new_shift.date = form.date.data
        new_shift.start_time = form.start_time.data
        new_shift.end_time = form.end_time.data
        new_shift.comment = form.comment.data

        db.session().commit()

        if not shift_id:
            #automagically conjure a blank report upon shift creation
            report = Report(new_shift.shift_id, current_user.user_id)
            report.comments = form.comment.data
            db.session().add(report)
            db.session().commit()

    return redirect( url_for('list_shifts') )

@app.route('/shifts/<int:shift_id>', methods=['GET'])
@login_required
def remove_shift(shift_id):
    if current_user.is_suurmartta():
        shift_to_remove = Guardshift.query.get_or_404(shift_id)

        if shift_to_remove:
            db.session().delete(shift_to_remove)
            db.session().commit()

    return redirect(url_for('list_shifts'))