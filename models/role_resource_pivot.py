from app import db


role_resource = db.Table('role_resource',
    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'), primary_key=True),
    db.Column('resource_id', db.Integer, db.ForeignKey('resource.resource_id'), primary_key=True)
)