from repository.dept_repo import Dept_repo
from app import db
from marshmallow import ValidationError

class Department_BL():
    @staticmethod
    def get_department(departments_id):
        if not departments_id:
            raise ValidationError("Provide Valid department id")
        
        dept = Dept_repo.get_department_repo(departments_id)
        if not dept:
            raise ValidationError("Department doesn't exist")
        
        schema = Dept_repo.get_dept_schema()
        result = schema.dump(dept)

        return result
    
    @staticmethod
    def delete_department(dept_id):
        dept = Dept_repo.get_dept_id(dept_id)
        if dept:
            id= Dept_repo.delete_department(dept)
            db.session.commit()
            return id
        else:
            raise ValidationError("department doesn't exist")
        
    @staticmethod
    def get_all_dpt():
        dept = Dept_repo.get_all_departments()

        schema = Dept_repo.get_dept_schema(single = False)

        serialized_result = schema.dump(dept)
        return serialized_result
    
    @staticmethod
    def add_dept(dep_name):
        
        if dep_name is None:
            return {'error': 'No data provided'}, 400
        
        existing_dep = Dept_repo.check_dep(dep_name)
        if existing_dep:
            return {"message": "Department already exists"}, 400
       
    
        try:
                new_dep = Dept_repo.create_department(dep_name)
                db.session.commit()
                return new_dep
        except Exception as e:
            db.session.rollback()
            return {'message': f"An error occurred: {str(e)}"}, 500

        
    
