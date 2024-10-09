from models.role_model import Role
from app import ma


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_relationships = True
        load_instance = True

