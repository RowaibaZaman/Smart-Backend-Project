from repository.dept_repo import Dept_repo
from app import db

class Department_BL():
    @staticmethod
    def get_department(args):
        departments_id = args.get('department_id')
        return Dept_repo.get_department_repo(departments_id)
    
    @staticmethod
    def delete_department(dept_id):
        id= Dept_repo.delete_department(dept_id)
        db.session.commit()
        return id
    
    @staticmethod
    def get_all_dpt():
        dept = Dept_repo.get_all_departments()

        schema = Dept_repo.get_project_schema(single= False)

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

        
    
