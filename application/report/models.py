from application import db

class Report(db.Model):
    report_id = db.Column(db.Integer, primary_key=True)
    shift_id = db.Column(db.Integer, db.ForeignKey('guardshift.shift_id'), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('account.user_id'), nullable=False)
    comments = db.Column(db.Text)
    finished = db.Column(db.Boolean, default=False)

    def __init__(self, shift, creator, comments) -> None:
        self.shift_id = shift
        self.creator_id = creator
        self.comments = comments
