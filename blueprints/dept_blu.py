from flask import Blueprint, jsonify
from bl.dept_bl  import Department_BL
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import ValidationError
    
department_bp = Blueprint('department', __name__)

@department_bp.route('/get_department', methods=['GET'])
@use_args({
    "department_id": fields.Int(required=True)  

}, location='query')

def get_department_route(args):
    """ return the department if it exist
    return deptamnet name and id"""

    department_id = args.get('department_id')
    try:
        result = Department_BL.get_department(department_id)

        return jsonify(result)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e), "message": "An error occurred"}), 500




@department_bp.route('/create_department', methods=['POST'])
@use_args({
    "dep_name": fields.Str(required=True)  

}, location='json')
def create_department_route(args):
    """ Add new department """

    department_name = args.get('dep_name')
    result = Department_BL.add_dept(department_name)
    return jsonify(result), 201


@department_bp.route('/delete_department', methods= ['DELETE'])
@use_args({
    "dept_id": fields.Int(required=True)  

}, location='query')
def delete_department_route(args):
    """ Delete the existingdept via id
    args: dept id"""

    dept_id = args.get('dept_id')
    try:
      result = Department_BL.delete_department(dept_id)
      return result
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        
        return jsonify({"error": str(e), "message": "An error occurred"}), 500
    

@department_bp.route('/get_all_dept', methods = ['GET'])
def get_all_Dept():
    """ return all the departments"""
    result = Department_BL.get_all_dpt()
    return jsonify(result)