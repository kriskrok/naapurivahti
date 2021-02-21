from application import db

class Picture(db.Model):
    picture_id = db.Column(db.Integer, primary_key=True)
    observation_id = db.Column(db.Integer, db.ForeignKey('observation.observation_id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('account.user_id'), nullable=True)
    name = db.Column(db.Text)
    data = db.Column(db.LargeBinary)

    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data