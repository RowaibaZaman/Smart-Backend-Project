from repository.role_allocation_repo import Role_Allocation_Repo
from repository.resource_repo import Resource_repo
from app import db
from marshmallow import ValidationError


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
           return result
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

