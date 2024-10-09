
from app import db

project_task = db.Table('project_task',
    db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
)
    