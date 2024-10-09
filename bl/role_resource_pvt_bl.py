from repository.rol_resource_pivot_repo import role_resource_repo
from app import db

class role_resource_BL:
    @staticmethod
    def assign_role_to_resource(resource_id, role_id):
        resource, role = role_resource_repo.add_role_to_resource(resource_id, role_id)
        
        if resource and role:
                resource.roles.append(role)  
                db.session.commit()
                return True
        return False
        
    @staticmethod
    def fetch_roles_for_resource(resource_id):
        roles = role_resource_repo.get_roles_for_resource(resource_id)
        if roles:
            return [role.role_name for role in roles.roles]
        return None
        