

from models.Resoucre_model import Resource
from sqlalchemy.orm import joinedload
from app import db
from schemas.ResourceSchema import ResourceSchema
from models.Resourcealloctaion_model import ResourceAllocation
from models.task_model import Task


class Resource_repo:
    @staticmethod
    def check_resource_exists(resource_name):
            return Resource.query.filter_by(resource_name=resource_name).first()
    
    @staticmethod
    def get_profile(resource_id):
        resource = db.session.query(Resource).options(
            joinedload(Resource.resource_allocation)
            .joinedload(ResourceAllocation.taskss)
            .joinedload(Task.project)
        ).filter_by(resource_id=resource_id).first()

        return resource
            
    @staticmethod
    def check_resource_id(resource_id):
          result = Resource.query.get(resource_id)
          return result
    
    @staticmethod
    def add_Resource(args):
        new_resource = Resource(**args)
        db.session.add(new_resource)
        return new_resource
    
    @staticmethod
    def get_resource_by_id(id):
            resource = Resource.query.get(id)
            print(f"Querying resource with ID: {id}, Result: {resource}")
            return resource

    @staticmethod
    def get_all_resource():
        result= Resource.query.all()
        return result
            

    @staticmethod
    def delete_resource_repo(resource_id):
        resource = Resource.query.get(resource_id)
        
        return resource
        
    @staticmethod
    def get_resource_schema(single=True):
                """Create and return the schema instance."""
                return ResourceSchema() if single else ResourceSchema(many=True)


            