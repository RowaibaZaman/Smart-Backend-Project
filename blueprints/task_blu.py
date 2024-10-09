from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from bl.task_bl import Task_BL
from marshmallow import ValidationError

task_bp = Blueprint('task', __name__)

@task_bp.route('/get_task_by_id', methods=['GET'])

@use_args({
    "task_id":fields.Int(required =True)
}, location = 'query')

def get_task_route(args):
    task_id = args.get('task_id')
    task = Task_BL.get_task(task_id)
    return jsonify(task), 200

    

@task_bp.route('/all_tasks', methods=['GET'])
def get_all_tasks_route():
    tasks = Task_BL.get_all_tasks()
    return jsonify(tasks)


@task_bp.route('/add_task', methods=['POST'])
@use_args({
    "task_name": fields.Str(required=True),
    "start_date": fields.Str(required=True),  
    "end_date": fields.Str(required=True),    
    "project_id": fields.Int(required=True),
    "description": fields.Str(required=True)
}, location='json')


def add_task_route(args):
    try:
        result = Task_BL.add_task(args)
        return jsonify(result), 201
    except Exception as e:
            return jsonify({"error": str(e)}), 500

@task_bp.route('/delete_task', methods = ["DELETE"])
@use_args({
    "task_id": fields.Int(required = True)}, 
    location = 'query'
)
def delete_task(args):
    task_id = args.get('task_id')
    print(f"Received task_id: {task_id}")
    result = Task_BL.delete_task_bl(task_id)
    return jsonify(result)

@task_bp.route("/get_all_task_with_no_resource", methods = ['GET'])
def get_all_task_with_no_resource():
    tasks = Task_BL.task_with_no_resource()
    return jsonify(tasks)

@task_bp.route('/add_new_task', methods= ['POST'])
@use_args({
    "resource_id": fields.Int(required= True),
    "task_name": fields.Str(required=True),
    "start_date": fields.Str(required=True),  
    "end_date": fields.Str(required=True),    
    "description": fields.Str(required=True)
})
def add_new_task_and_allocation(args):
    """new task and allocation"""
    try:
        result = Task_BL.add_new_task_bl(args)
        return result
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400 
    except Exception as e:
        return jsonify({"error": str(e)}), 500