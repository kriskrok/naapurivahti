from application import db

shiftmembers = db.Table('shiftmembers',
                db.Column('member_id', db.Integer, db.ForeignKey('account.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False),
                db.Column('shift_id', db.Integer, db.ForeignKey('guardshift.shift_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False))

class Guardshift(db.Model):
    shift_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time(timezone=False))
    end_time = db.Column(db.Time(timezone=False))

    def __init__(self, date, start, end) -> None:
        self.date = date
        self.start_time = start
        self.end_time = end
