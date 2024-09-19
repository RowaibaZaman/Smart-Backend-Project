# from repository.project_repo import Project_repo
from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from datetime import datetime
from bl.project_bl import Project_BL

project_bp = Blueprint('project', __name__ )

@project_bp.route('/add_project', methods =['POST'])
@use_args({
    "project_name": fields.Str(required = True),
    "start_date" : fields.Str(required = True),
    "end_date": fields.Str(required = True),
    "description": fields.Str(required =True)
}, location = 'json')

def add_project(args):
    print('data is in blueprints')
 
    result = Project_BL.add_project_bl(args)
    return jsonify(result), 201

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


