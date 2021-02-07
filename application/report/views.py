from flask import render_template
from application import app
#from application import db

@app.route('/reports')
def reports_list():
	return render_template('reports_list.html')