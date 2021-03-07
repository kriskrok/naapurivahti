from flask import render_template
from flask_login import login_required

from application import app, db
from application.report.models import Report
from application.observation.models import Observation

@app.route('/reports/list')
@login_required
def reports_list():
	repo = Report.get_reportlisting()
	print('Terveisiä täältä', repo)
	return render_template('reports_list.html', reports = repo)

@app.route('/reports/<int:report_id>')
@login_required
def list_report(report_id):
	match = Report.query.get(report_id)
	if match:
		print('Löytyikö', report_id, match)
		related_observations = Observation.query.filter_by(report_id=match.report_id).order_by('timing').all()
		#related_observations = db.session.query(Observation).filter(Observation.report_id == report_id).all()
		#vara = db.session().query(Observation).filter_by(report_id = '1').all()
		print('TulokseMME', related_observations)



		


	return render_template('list_report.html', report_id = report_id, observations = related_observations)