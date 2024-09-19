

from app import db

class ResourceAllocation(db.Model):
    __tablename__ = 'resource_allocation'
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id'))  
    allocation_date = db.Column(db.Date) 
    task_id = db.Column(db.Integer, db.ForeignKey('task.id')) 

    taskss = db.relationship('Task', back_populates = 'Resource_Allocation')
    resource = db.relationship('Resource', back_populates='resource_allocation')
