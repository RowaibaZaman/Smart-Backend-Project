from app import db
from schemas.Role_allocation_schema import Role_AllocationSchema
from models.role_allocation_model import RoleAllocation
from models.Resoucre_model import Resource
from models.role_model import Role
from flask import  jsonify
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload


class Role_Allocation_Repo:
    @staticmethod
    def add_role_allocation(args):
        try:
            new_allocation = RoleAllocation(**args)
            db.session.add(new_allocation)
        
        except ValidationError as ve:
            return jsonify(ve.messages)
        
        except Exception as e:
            db.session.rollback()
            raise e  
        
    @staticmethod
    def check_role_allocation(resource_id, role_id):
        """Check if the role allocation already exists."""
        existing_allocation = RoleAllocation.query.filter_by(resource_id=resource_id, role_id=role_id).first()
        return existing_allocation 
    
    @staticmethod
    def delete_role_allocation_repo(id):
        allocation_to_delete = RoleAllocation.query.filter_by(role_allocation_id = id).first()
        if allocation_to_delete:
            db.session.delete(allocation_to_delete)
            return True
        else:
            return False
        
    @staticmethod
    def return_role_repo(id):
        result = db.session.query(RoleAllocation).options(joinedload(RoleAllocation.role)).filter(RoleAllocation.resource_id == id).first()  # Get the first result, or None if not found

        if result:
                return result.role.role_name  # Access the role name
        else:
                return None
        
    @staticmethod
    def get_roleallocation_schema(single= True):
                """Create and return the schema instance."""
                return Role_AllocationSchema() if single else Role_AllocationSchema(many=True)

    @staticmethod
    def all_allocation_repo():
         roles = db.session.query(RoleAllocation).join(Resource).join(Role).all()
         return roles

    
