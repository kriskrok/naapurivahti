from application import db
from sqlalchemy.sql import text

class Report(db.Model):
	report_id = db.Column(db.Integer, primary_key=True)
	shift_id = db.Column(db.Integer, db.ForeignKey('guardshift.shift_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
	creator_id = db.Column(db.Integer, db.ForeignKey('account.user_id'), nullable=False)
	comments = db.Column(db.Text)
	finished = db.Column(db.Boolean, default=False)
	

	def __init__(self, shift, creator) -> None:
		self.shift_id = shift
		self.creator_id = creator
    
	@staticmethod
	def get_reportlisting():
		stmt = text('SELECT account.username, report.report_id, report.comments, '
		+ 'guardshift.date, guardshift.start_time, guardshift.end_time '
		+ 'FROM report, guardshift, account '
		+ 'WHERE account.user_id = report.creator_id '
		+ 'AND report.shift_id = guardshift.shift_id')

		res = db.engine.execute(stmt)	#type: sqlalchemy.engine.result.ResultProxy

		response = []
		for row in res:
			response.append(
				{'username':row[0], 'id':row[1], 'comments':row[2], 'date':row[3], 'start_time':row[4], 'end_time':row[5]
			})

		return response