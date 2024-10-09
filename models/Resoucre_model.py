from app import db
from models.role_resource_pivot import role_resource
from models import *
from models.role_model import Role
from models.Resourcealloctaion_model import ResourceAllocation
from models.task_model import Task


class Resource(db.Model):
    __tablename__ = 'resource'  
    
    resource_id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(50), nullable=False)  
    dep_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))
    
    resource_allocation = db.relationship(ResourceAllocation, back_populates='resource')
    # role_allocation = db.relationship('RoleAllocation', back_populates='resource')

    # Many-to-many relationship to Role through role_resource
    roles = db.relationship(Role, secondary=role_resource, back_populates ='role_resources') #backref=db.backref('resources', lazy='dynamic')