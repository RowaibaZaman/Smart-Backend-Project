from models.role_allocation_model import RoleAllocation
from schemas.ResourceSchema import ResourceSchema
from schemas.RoleSchema import RoleSchema
from app import ma


class Role_AllocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoleAllocation
        include_relationships = True
        load_instance = True
     

    resource = ma.Nested(ResourceSchema, only = ['resource_name'])
    role = ma.Nested(RoleSchema, only =['role_name'])

