from app import db

class ResourceAllocation(db.Model):
    __tablename__ = 'resource_allocation'
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id'), nullable=True)  
    allocation_date = db.Column(db.Date) 
    task_id = db.Column(db.Integer, db.ForeignKey('task.id')) 
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), nullable=True)

    taskss = db.relationship('Task', back_populates = 'Resource_Allocation')
    resource = db.relationship('Resource', back_populates='resource_allocation')
    project = db.relationship('Project', back_populates= 'resource_allocation')
