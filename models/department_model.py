

from app import db

class Department(db.Model):
    __tablename__ = 'department'
    dept_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dep_name = db.Column(db.String(10), nullable=False)

    # employee = db.relationship('Employee', back_populates='dept')


