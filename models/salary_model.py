from app import db

class Salary(db.Model):
    __tablename__ = 'salary'
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id') , nullable=False)
    salary = db.Column(db.Numeric, nullable=False)
    
    resource = db.relationship('Resource', backref='salary')