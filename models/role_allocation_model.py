
from app import db


class RoleAllocation(db.Model):
    __tablename__ = 'role_allocation'

    role_allocation_id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id'))  
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))

    role = db.relationship('Role', back_populates='role_allocation')
    resource = db.relationship('Resource',  backref=db.backref('role_allocation', lazy=True))

