from repository.role_allocation_repo import Role_Allocation_Repo
from repository.resource_repo import Resource_repo
from app import db
from marshmallow import ValidationError
from enumss import RoleEnum



class RoleAllocation_BL:

    @staticmethod
    def add_role_allocation_bl(args):
        resource_id = args.get('resource_id')
        role_id = args.get('role_id')

        # Check if the allocation already exists using the repo function
        if Role_Allocation_Repo.check_role_allocation(resource_id, role_id):
            raise ValidationError("Role allocation already exists.")
        
        check = Resource_repo.check_resource_id(resource_id)
        if not check:
            raise ValidationError("Resource id doesn't exists")
        
        new_r_allocation = Role_Allocation_Repo.add_role_allocation(args)
        db.session.commit()

        schema = Role_Allocation_Repo.get_roleallocation_schema()
        new_ra = schema.dump(new_r_allocation)

        return {"message": "Role Allocated Successfully"}
    

    @staticmethod
    def delete_role_allocation_bl(id):
        result = Role_Allocation_Repo.delete_role_allocation_repo(id)
        if result:
            db.session.commit()
            return {"message": "Role Allocation Deleted Successfully"}
        else:
            raise ValidationError("Role allocation doesn't exist.")
    
    @staticmethod
    def return_role_bl(id):
        result = Role_Allocation_Repo.return_role_repo(id)
        if result:
           return result.role.role_name 
        else:
            raise ValidationError("Id is not alocated to any role")

    @staticmethod
    def all_role_bl():
        result = Role_Allocation_Repo.all_allocation_repo()
        if result:
            schemas = Role_Allocation_Repo.get_roleallocation_schema(single=False)
            dump = schemas.dump(result)

            return dump
        else:
            raise ValidationError("No allocations found.")
        
    @staticmethod
    def assign_role_to_resource(assigner_resource_id, assignee_resource_id, role_id):
        try:
            #chk forresource
            resource_id = Resource_repo.check_resource_id(assignee_resource_id)
            if not resource_id:
                raise ValidationError("Assignee Resource doesn't exist")
            
            check_resource, manager_role = Role_Allocation_Repo.is_manager(assigner_resource_id)
            
            if not check_resource or not manager_role:
                raise ValidationError("Assigner resource or Manager role not found")
            
            # Check if assigner has a manager role
            is_manager = any(role.role_name == RoleEnum.MANAGER.value for role in check_resource.roles)
            if not is_manager:
                raise ValidationError("Only a manager can assign roles")
            
            if Role_Allocation_Repo.check_if_resource_allocated(assignee_resource_id, role_id):
                raise ValidationError("The role is already allocated to the resource")
            # Add role allocation for the assignee
            role_allocation = Role_Allocation_Repo.add_role_allocations(assignee_resource_id, role_id)

        # Commit the changes
       
            db.session.commit()
        except Exception as e:
            db.session.rollback()  
            raise Exception(f"Database commit failed: {str(e)}")
        
        return {"message": "Role assigned successfully"}
    
