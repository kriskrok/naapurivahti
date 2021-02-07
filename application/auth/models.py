from application import db

class Account(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(63), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	role = db.Column(db.Integer, nullable=False)
	created_on = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
	last_login = db.Column(db.DateTime(timezone=True), onupdate=db.func.current_timestamp()) #onupdate for safekeeping

	def __init__(self, email, username, password) -> None:
		self.email = email
		self.username
		self.password = password
		self.role = 1
