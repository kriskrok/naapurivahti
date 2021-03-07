from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.observation.models import Observation
from application.observation.forms import CreateObservationForm

@app.route('/observations/new')
@login_required
def open_observationform():
    observation_id = request.args.get('observation_id')
    form = CreateObservationForm()

    if observation_id: #True if we're updating 
        observation = Observation.query.get(observation_id)

        form.comment.data = observation.comment
        form.timing.data = observation.timing
        form.requires_action.data = observation.requires_action


    report_id = request.args.get('report_id')
    return render_template('observation_form.html',  observationform = form, report_id=report_id, observation_id = observation_id)

@app.route('/observations/new/', methods=['POST'])
@login_required
def save_observation():
    form = CreateObservationForm(request.form)

    report_id =  request.args.get('report_id')
    observation_id =  request.args.get('observation_id')

    print('\n\n\nHeippa täältä uudesta havainnosta!', observation_id, report_id, '\n\n\n')

    if not form.validate():
        return render_template('observation_form.html',  observationform = form, report_id=report_id, observation_id = observation_id)

    if observation_id: #True if we're updating
        new_observation = Observation.query.get(observation_id)
    else: #True if we're creating new
        new_observation = Observation(report=report_id, timing=form.timing.data,
                            comment=form.comment.data, action=form.requires_action.data)
        new_observation.set_author(current_user.get_id())
        db.session.add(new_observation)

    new_observation.timing = form.timing.data
    new_observation.comment = form.comment.data
    new_observation.requires_action = form.requires_action.data

    db.session.commit()

    return redirect(url_for('list_report', report_id=report_id))

@app.route('/observations/<int:observation_id>', methods=['GET'])
@login_required
def remove_observation(observation_id):
    observation_to_remove = Observation.query.get_or_404(observation_id)

    if observation_to_remove:
        db.session().delete(observation_to_remove)
        db.session().commit()
        print('Terminated, rejoice!\n')

    return redirect(url_for('list_report', report_id=request.args.get('report_id')))
