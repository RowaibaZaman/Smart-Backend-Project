from app import db

class Resource(db.Model):
    __tablename__ = 'resource'  
    
    resource_id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(50), nullable=False)  
    dep_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))
    
    resource_allocation = db.relationship('ResourceAllocation', back_populates='resource')
    # role_allocation = db.relationship('RoleAllocation', back_populates='resource')
