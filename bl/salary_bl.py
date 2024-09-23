from repository.salary_repo import SalaryRepo
from app import db
from marshmallow import ValidationError
from flask import  jsonify

class SalaryBL:


    @staticmethod
    def add_salary(args):
        check = SalaryRepo.resource_has_salary(args.get('resource_id'))
        if check:
                raise ValidationError("Salary is already Assigned you can update salary")

        try: 
            result = SalaryRepo.add_salary(args)
            db.session.commit()

            # schema = SalaryRepo.get_salary_schema(single = False)

            # result1 = schema.dump(result)
            if result:
                return {"message": "Salary added successfully" }, 201
            

        except Exception as e:
            db.session.rollback()
            return jsonify({"Resource doesn't exists"})
