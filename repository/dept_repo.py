
from models.department_model import Department
from app import db
from schemas.DepartmentSchema import DepartmentSchema
from marshmallow import ValidationError


class Dept_repo:

    @staticmethod
    def get_dept_schema(single=True):
                """Create and return the  Schema instance."""
                return DepartmentSchema() if single else DepartmentSchema(many=True)

    @staticmethod
    def check_dep(dept_name):
        """ check existing dept by namedepartment name"""
        if dept_name:
            return Department.query.filter_by(dep_name = dept_name).first()
        
    @staticmethod
    def get_department_repo(department_id):
        """ Get the dept by id"""

        department = Department.query.get(department_id)
        return department
 
    @staticmethod
    def get_all_departments():
        """ Get all departments"""
        result=  Department.query.all()
        return result
    

    @staticmethod
    def create_department(name):
        """ Add new department"""
    
        new_department = Department(dep_name=name)
        db.session.add(new_department)
        
        return {'message': "Department added successfully"}, 201

    @staticmethod
    def delete_department(department):
        """ Delete the existing department"""
        
        db.session.delete(department)

        return {"message": "Department deleted Sucsessfully"}
  
    @staticmethod 
    def get_dept_id(dept_id):
        department = Department.query.get(dept_id)
        return department
         
    