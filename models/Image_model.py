from flask_sqlalchemy import SQLAlchemy
from models.Resoucre_model import Resource
from app import db


class ResourceImage(db.Model):
    __tablename__ = 'resource_image'
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id', ondelete='CASCADE'), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)
    
    # Define the relationship
    resource = db.relationship('Resource', backref=db.backref('images', lazy=True, cascade="all, delete-orphan"))