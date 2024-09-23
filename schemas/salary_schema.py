from models.salary_model import Salary
from app import ma

class SalarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salary
        include_fk = True
        include_relationships = True