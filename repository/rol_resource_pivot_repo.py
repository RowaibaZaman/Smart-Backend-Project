from models.Resoucre_model import Resource
from models.role_model import Role
from app import db

class role_resource_repo:
    @staticmethod
    def add_role_to_resource(resource_id, role_id):
        resource = Resource.query.get(resource_id)
        role = Role.query.get(role_id)
        
        return resource, role
        
    @staticmethod
    
    def get_roles_for_resource(resource_id):
        resource = Resource.query.get(resource_id)
        
        return resource
    