from app import db
from schemas.Role_allocation_schema import Role_AllocationSchema
from models.role_allocation_model import RoleAllocation
from models.Resoucre_model import Resource
from repository.resource_repo import Resource_repo
from models.role_model import Role
from flask import  jsonify
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload
from enumss import RoleEnum


class Role_Allocation_Repo:
    @staticmethod
    def get_roleallocation_schema(single= True):
                """Create and return the schema instance."""
                return Role_AllocationSchema() if single else Role_AllocationSchema(many=True)

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
        """ Delete the role Aloocation"""
        allocation_to_delete = RoleAllocation.query.filter_by(role_allocation_id = id).first()
        if allocation_to_delete:
            db.session.delete(allocation_to_delete)
            return True
        else:
            return False
        
    @staticmethod
    def return_role_repo(id):
        """ retrun the role associated with the resource"""
        result = db.session.query(RoleAllocation).options(joinedload(RoleAllocation.role)).filter(RoleAllocation.resource_id == id).first()  # Get the first result, or None if not found
        return result 

        
    
    @staticmethod
    def all_allocation_repo():
         roles = db.session.query(RoleAllocation).join(Resource).join(Role).all()
         return roles


    @staticmethod
    def add_role_allocations(assignee_resource_id, role_id):
        role_allocation = RoleAllocation(resource_id=assignee_resource_id, role_id=role_id)
        db.session.add(role_allocation)

        return role_allocation
    

    # @staticmethod
    # def is_manager(resource_id):
    #     """ check if assigner is a manager"""

    #     try:
    #         # resource 
    #         check_resource = Resource_repo.check_resource_id(resource_id)
    #         # print(f"Checking for resource with ID: {resource_id} (Type: {type(resource_id)})")
    #         # print(f"Type of resource_id being passed: {type(resource_id)}")

    #         # chk if manager
    #         manager_role = Role.query.filter_by(role_name=RoleEnum.MANAGER.value).first()
            
    #         if not manager_role:
    #             print("No Manager role found in the database")
    #             return False
                
    #         # Check if the manager role exists in the resource's roles
    #         # is_manager = manager_role in check_resource.roles   # this fails b/c manager_role is the object returned by Role
    #         # print(f"Manager role check: {is_manager}")
    #         # return is_manager
        
    #         is_manager = any(role.role_name == RoleEnum.MANAGER.value for role in check_resource.roles)
    #         print(f"Manager role check for resource {resource_id}: {is_manager}")
    #         return is_manager
                
    #     except Exception as e:
    #         print(f"An error occurred during manager check: {e}")
    #         return False
        

    @staticmethod
    def is_manager(resource_id):
        """ check if assigner is a manager"""

        try:
          
            check_resource = Resource_repo.check_resource_id(resource_id)
           
            manager_role = Role.query.filter_by(role_name=RoleEnum.MANAGER.value).first()
            
            return check_resource, manager_role
                
        except Exception as e:
            print(f"An error occurred during manager check: {e}")
            return False

    @staticmethod
    def check_if_resource_allocated(resource_id, role_id):
        """
        Check if a role is already allocated to the specified resource.
        """
        
        existing_allocation = RoleAllocation.query.filter_by(resource_id=resource_id, role_id=role_id).first()
        return existing_allocation 