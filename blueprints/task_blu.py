from flask import Blueprint, request, jsonify
from webargs import fields
from webargs.flaskparser import use_args
# from schemas.TaskSchema import tasks_schema, task_schema
from bl.task_bl import Task_BL
# from bl.task_bl import add_task,get_all_tasks, delete_task_bl


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
    result = Task_BL.add_task(args)
    return jsonify(result), 201


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


###################################################
@task_bp.route("/get_all_task_with_no_resource", methods = ['GET'])
def get_all_task_with_no_resource():
    tasks = Task_BL.task_with_no_resource()
    return jsonify(tasks)