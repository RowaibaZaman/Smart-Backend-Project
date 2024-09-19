from app import db



class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(40), nullable = False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))


    project = db.relationship('Project', back_populates = 'tasks')
    Resource_Allocation = db.relationship('ResourceAllocation', back_populates = 'taskss', lazy = True)
