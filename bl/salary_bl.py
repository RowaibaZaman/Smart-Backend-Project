from repository.salary_repo import SalaryRepo
from app import db
from marshmallow import ValidationError
from flask import  jsonify
from schemas.salary_schema import SalarySchema

class SalaryBL:


    @staticmethod
    def add_salary(args):
        check = SalaryRepo.resource_has_salary(args.get('resource_id'))
        if check:
                raise ValidationError("Salary is already Assigned you can update salary")

        try: 
            result = SalaryRepo.add_salary(args)
            db.session.commit()

            if result:
                return {"message": "Salary added successfully" }, 201
            

        except Exception as e:
            db.session.rollback()
            return jsonify({"Resource doesn't exists"})
        
    @staticmethod
    def get_all_salaries():
            try:
                # Retrieve all salary records from the repository
                salaries = SalaryRepo.get_salaries()

                # Serialize the result using the SalarySchema
                schema = SalaryRepo.get_salary_schema(single=False)
                serialized_data = schema.dump(salaries)

                return {"salaries": serialized_data}, 200

            except Exception as e:
                return {"error": str(e)}, 500
            
    
    @staticmethod
    def update_salary_bl(args): 
        resource_id = args.get('resource_id')
        salary = args.get('salary')

        # Check if the salary already exists
        existing_salary = SalaryRepo.resource_has_salary(resource_id)

        schema = SalaryRepo.get_salary_schema()

        if existing_salary:
            # If it exists, update the salary
            updated_salary = SalaryRepo.update_salary_repo(resource_id, salary)
            return {"message": "Salary updated successfully!", "salary": schema.dump(updated_salary)}, 200
        else:
            raise ValidationError("Salary is not assigned; add salary to resource.")