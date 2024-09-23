from app import db
from models.salary_model import Salary
from marshmallow import ValidationError
from schemas.salary_schema import SalarySchema

class SalaryRepo:

    @staticmethod
    def add_salary(args):

        new_salary = Salary(**args)
        db.session.add(new_salary)

        return new_salary
    
    @staticmethod
    def resource_has_salary(resource_id):
        return db.session.query(Salary).filter_by(resource_id=resource_id).first() is not None
    
    @staticmethod
    def get_salary_schema(single=True):
                """Create and return the schema instance."""
                return SalarySchema() if single else SalarySchema(many=True)
    
    @staticmethod
    def get_salaries():
        salaries = db.session.query(Salary).all()
        return salaries
    
   
    @staticmethod
    def update_salary_repo(resource_id, salary_amount):
        # Retrieve the existing salary record
        existing_salary = db.session.query(Salary).filter_by(resource_id=resource_id).first()
        
        if existing_salary:
            existing_salary.salary = salary_amount
            
            return existing_salary
        else:
            raise ValueError("Salary record not found.")
