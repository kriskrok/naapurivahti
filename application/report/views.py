from flask import render_template
from flask.helpers import url_for
from flask_login import login_required
from werkzeug.utils import redirect

from application import app, db
from application.report.models import Report
from application.observation.models import Observation
from application.auth.models import Account

@app.route('/reports/list')
@login_required
def reports_list():
	repo = Report.get_reportlisting()
	return render_template('reports_list.html', reports = repo)

@app.route('/reports/<int:report_id>')
@login_required
def list_report(report_id):
	if not Report.query.get(report_id):
		return redirect( url_for('reports_list') )
		
	related_observations = db.session.query(Observation, Account).join(Account, Observation.author_id == Account.user_id).filter(Observation.report_id == report_id).order_by('timing').all()

	return render_template('list_report.html', report_id = report_id, observations = related_observations)
