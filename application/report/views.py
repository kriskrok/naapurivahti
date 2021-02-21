from flask import render_template
from flask_login import login_required
from application import app

@app.route('/reports')
@login_required
def reports_list():
	return render_template('reports_list.html')