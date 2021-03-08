from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class Account(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(63), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	role = db.Column(db.Integer, nullable=False)
	created_on = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp(), nullable=False)
	last_login = db.Column(db.DateTime(timezone=False), onupdate=db.func.current_timestamp())

	def __init__(self, email, username) -> None:
		self.email = email
		self.username = username
		self.role = 1

	def get_id(self):
		return self.user_id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	def is_suurmartta(self):
		return self.role == 42

	def set_password(self, password):
		self.password = generate_password_hash(password, method='sha256', salt_length=16)

	def check_password(self, password):
		"""Be mindfull that this eats hashes in the following form: method$salt$hash"""
		return check_password_hash(self.password, password)