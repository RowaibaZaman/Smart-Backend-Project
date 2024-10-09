 
from app import db
from repository.task_repo import Task_repo
from repository.resource_repo import Resource_repo
from marshmallow import ValidationError
from flask import jsonify

class Task_BL:
    @staticmethod
    def get_task(task_id):
        task = Task_repo.get_task_by_id(task_id)
        if task:
            task_dict = Task_repo.get_task_schema.dump(task)
            if 'resource' in task_dict:
                del task_dict['resource']
            return task_dict
        else:
            return {"message":"task doesn't exist"}
    @staticmethod
    def delete_task_bl(task_id):
        try:
            task = Task_repo.delete_task_repo(task_id)
            if task:
                db.session.commit()
                return {"message": "Task deleted successfully"}, 200
            else:
                return {"message": "Task not found"}, 404
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    
    @staticmethod
    def add_task(args):

        if not args:
            return {'message': 'No data entered'}
        
        existing_task = Task_repo.check_task(args.get("task_name"))
        if existing_task:
            return {"message": "Task already exists"}, 400

        try:
            new_task = Task_repo.add_task_repo(args)
            if new_task:
                db.session.commit()
                return {'message': "Task added successfully"}, 201

        except Exception as e:
            db.session.rollback()
            return {'message': f"An error occurred: {str(e)}"}, 500

    @staticmethod
    def get_all_tasks():
            try:
                tasks = Task_repo.get_all_task_repo()   
                schema = Task_repo.get_task_schema(single =False)
                serialized_tasks = schema.dump(tasks)

                return serialized_tasks

            except Exception as e:
                return {'message': f"An error occurred: {str(e)}"}, 500
    
    @staticmethod
    def task_with_no_resource():
        tasks = Task_repo.task_with_no_resource_repo()
        tasks_list = [{'id': task.id, 'task_name': task.task_name} for task in tasks]
        return tasks_list
    
    @staticmethod
    def add_new_task_bl(args):
        resource_id = args.get('resource_id')
        #check resoruce
        if resource_id:
            resource = Resource_repo.check_resource_id(resource_id)
            if not resource:
                raise ValidationError("Resource not found")
            
        #check if task exists
        existing_task = Task_repo.check_task(args.get("task_name"))
        if existing_task:
            raise ValidationError("Task already exists")
                        
        task = Task_repo.add_new_task_repo(args, resource_id )
        if task:
            db.session.commit()
        return jsonify({"message": "Task and Resource Allocation created successfully"}), 201