from app import db

    
class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)

    
    tasks = db.relationship('Task', back_populates = 'project' )
    # ResourceAllocation = db.relationship("ResourceAllocation", back_populates = 'project')
