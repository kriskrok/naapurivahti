from flask import render_template
from flask_login import login_required

from application import app
from application.report.models import Report

@app.route('/reports/list')
@login_required
def reports_list():
	repo = Report.get_reportlisting()
	print('Terveisiä täältä', repo)
	return render_template('reports_list.html', reports = repo)
