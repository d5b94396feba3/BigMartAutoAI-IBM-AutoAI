from src import db


class DatasetThyroid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer, nullable=False)
    q2 = db.Column(db.Integer, nullable=False)
    q3 = db.Column(db.Integer, nullable=False)
    q4 = db.Column(db.Integer, nullable=False)
    q5 = db.Column(db.Integer, nullable=False)
    q6 = db.Column(db.Integer, nullable=False)
    q7 = db.Column(db.Integer, nullable=False)
    q8 = db.Column(db.Integer, nullable=False)
    q9 = db.Column(db.Integer, nullable=False)
    q10 = db.Column(db.Integer, nullable=False)
    q11 = db.Column(db.Integer, nullable=False)
    q12 = db.Column(db.Integer, nullable=False)
    q13 = db.Column(db.Integer, nullable=False)
    q14 = db.Column(db.Integer, nullable=False)
    q15 = db.Column(db.Integer, nullable=False)
    q16 = db.Column(db.Integer, nullable=False)
    q17 = db.Column(db.Integer, nullable=False)
    q18 = db.Column(db.Integer, nullable=False)
    q19 = db.Column(db.Integer, nullable=False)
    q20 = db.Column(db.Integer, nullable=False)
    res = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<DatasetThyroid %r>' % self.id


db.create_all()
