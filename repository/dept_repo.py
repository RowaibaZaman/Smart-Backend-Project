
from models.department_model import Department
from app import db
from schemas.DepartmentSchema import DepartmentSchema


class Dept_repo:
    @staticmethod
    def check_dep(dept_name):
        if dept_name:
            return Department.query.filter_by(dep_name = dept_name).first()
        
    @staticmethod
    def get_department_repo(department_id):
    
        if department_id:
                department = Department.query.get(department_id)
                if department:
                    # return dept_schema.jsonify(department)
                    return department
                else:
                    return {"message": "Department not found"}, 404
                
        else:
            return{'message': "Department doesn't exist"}
            
    @staticmethod
    def get_all_departments():
        
        result=  Department.query.all()
        return result
    

    @staticmethod
    def create_department(name):
    
        if not name:
            return {'error': 'Department name is required'}, 400

        new_department = Department(dep_name=name)
        db.session.add(new_department)
        
        return {'message': "Department added successfully"}, 201

    @staticmethod
    def delete_department(dept_id):
        # from model import Department
        from app import db

        department = Department.query.get(dept_id)
        if not department:
            
            return {"message": "Department does not exist"}, 404
        
        else:
            db.session.delete(department)
            return {"message": "Department deleted Sucsessfully"}
        
    @staticmethod
    def get_project_schema(single=True):
                """Create and return the ProjectSchema instance."""
                return DepartmentSchema() if single else DepartmentSchema(many=True)



