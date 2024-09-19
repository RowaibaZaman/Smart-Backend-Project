from models.role_model import Role
from app import db
from schemas.RoleSchema import RoleSchema

class Role_repo:
        @staticmethod
        def check_role_exists(role_name):
                
                return Role.query.filter_by(role_name=role_name).first()
        @staticmethod
        def add_Role_repo(args):
                new_role = Role(**args)
                db.session.add(new_role)
                return new_role
        
        @staticmethod
        def get_role_schema(single=True):
                """Create and return the schema instance."""
                return RoleSchema() if single else RoleSchema(many=True)



