# from datetime import datetime, timezone
from application import db
# from sqlalchemy import Table

shiftmembers = db.Table('shiftMembers',
                db.Column('member_id', db.Integer, db.ForeignKey('account.user_id'), nullable=False),   #Account.user_id
                db.Column('shift_id', db.Integer, db.ForeignKey('guardshift.shift_id'), nullable=False)) #Guardshift.id



class Guardshift(db.Model):
    shift_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time(timezone=False))
    end_time = db.Column(db.Time(timezone=False))

    def __init__(self, comment, date, start, end) -> None:
        self.comment = comment
        self.date = date
        self.start_time = start
        self.end_time = end


#CREATE TABLE guardshift (
#        shift_id SERIAL NOT NULL, 
#        date TIMESTAMP WITH TIME ZONE, 
#        start_time TIMESTAMP WITH TIME ZONE, 
#        end_time TIMESTAMP WITH TIME ZONE, 
#        PRIMARY KEY (shift_id)
#)


#2021-02-07 18:43:26,801 INFO sqlalchemy.engine.base.Engine {}
#2021-02-07 18:43:26,812 INFO sqlalchemy.engine.base.Engine COMMIT
#2021-02-07 18:43:26,814 INFO sqlalchemy.engine.base.Engine 
#CREATE TABLE "shiftMembers" (
#        member_id INTEGER NOT NULL, 
#        shift_id INTEGER NOT NULL, 
#        FOREIGN KEY(member_id) REFERENCES account (user_id), 
#        FOREIGN KEY(shift_id) REFERENCES guardshift (shift_id)
#)