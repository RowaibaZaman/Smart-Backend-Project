from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from bl.project_bl import Project_BL
from marshmallow import ValidationError

project_bp = Blueprint('project', __name__ )

#add project

@project_bp.route('/add_project', methods =['POST'])
@use_args({
    "project_name": fields.Str(required = True),
    "start_date" : fields.Str(required = True),
    "end_date": fields.Str(required = True),
    "description": fields.Str(required =True)
}, location = 'json')
def add_project(args):
    
    result = Project_BL.add_project_bl(args)
    return jsonify(result), 201


#get projects

@project_bp.route('/get_project', methods =['GET'])
def get_projecct():
    print('get project command running')

    result = Project_BL.get_project_bl()
    return jsonify(result), 201


@project_bp.route('/project_with_task_blu', methods=['GET'])
@use_args({"project_id": fields.Int(required=True)}, location='query')
def p_with_t(args):
    project_id = args.get('project_id')
    print(project_id)
    result = Project_BL.project_with_task_bl(project_id)
    return jsonify(result)


#update project

@project_bp.route('/update_project', methods=['PUT'])
@use_args({
    "project_id": fields.Int(required=True),         
    "project_name": fields.Str(required=False),      
    "start_date": fields.Str(required=False),
    "end_date": fields.Str(required=False),
    "description": fields.Str(required=False)
}, location='json')  

def update_project(args):
    project_id = args.get('project_id')  # Extract project_id from query parameters
    update_data = {k: v for k, v in args.items() if v is not None and k != 'project_id'}  # Extract fields to update
    result = Project_BL.update_project_bl(project_id, update_data)
    return jsonify(result)



#Pagination

@project_bp.route('/get_paginated_projects_blu', methods=['GET'])
@use_args({
    "limit": fields.Int(required=False, missing=2),
    "page": fields.Int(required=False, missing=1)
}, location='query')
def get_paginated_projects(args):
    """ Get paginated projects"""
    result = Project_BL.get_paginated_project_bl(args)
    return result


@project_bp.route('/add_new_project', methods = ['POST'])
@use_args({
    "project_name": fields.Str(required = True),
    "resource_id": fields.List(fields.Int(), required=True),
    "start_date" : fields.Str(required = True),
    "end_date": fields.Str(required = True),
    "description": fields.Str(required =True)
}, location = 'json') 
def add_new_project(args):
    try: 
        """ create new project and allocation"""
        result = Project_BL.new_project_bl(args)
        return result
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400 
    except Exception as e:
        return jsonify({"error": str(e)}), 500


