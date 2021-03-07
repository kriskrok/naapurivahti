from application import db

class Observation(db.Model):
    observation_id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.report_id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('account.user_id'), nullable=False)
    timing = db.Column(db.Time(timezone=False))
    comment = db.Column(db.Text)
    requires_action = db.Column(db.Boolean, default=False)

    def __init__(self, report=None, timing=None, comment=None, action=False) -> None:
        self.report_id = report
        self.timing = timing
        self.comment = comment
        self.requires_action = action
    
    def set_author(self, author_id):
        self.author_id = author_id