from models.salary_model import Salary
from app import ma
from schemas.ResourceSchema import ResourceSchema

class SalarySchema(ma.SQLAlchemyAutoSchema):
    resource = ma.Nested(ResourceSchema, only= ['resource_name'])

    class Meta:
        model = Salary
        include_fk = True
        include_relationships = True