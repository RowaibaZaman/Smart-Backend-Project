from app import db
from models.role_resource_pivot import role_resource
from models import *
from models.role_allocation_model import RoleAllocation

class Role(db.Model):
    __tablename__ = 'role'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)

    role_allocation = db.relationship(RoleAllocation, back_populates = 'role')
    # Many-to-many relationship to Resource through role_resource
    role_resources = db.relationship('Resource', secondary=role_resource, back_populates ='roles') #backref=db.backref('roles', lazy='dynamic')
     