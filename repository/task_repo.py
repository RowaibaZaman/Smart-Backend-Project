
from app import db
from models.task_model import Task
from models.Resourcealloctaion_model import ResourceAllocation
from datetime import datetime
from schemas.TaskSchema import TaskSchema
from flask import jsonify

class Task_repo:
        @staticmethod
        def get_task_schema(single=True):
                """Create and return the schema instance."""
                return TaskSchema() if single else TaskSchema(many=True)
        
        @staticmethod     
        def check_task(task_name):
                """Check if task_name already exists"""
                return Task.query.filter_by(task_name= task_name).first()

        @staticmethod
        def check_task_id(task_id):
             """ check if task exists"""
             check = Task.query.get(task_id)
             return check

        @staticmethod  
        def get_task_by_id(task_id):
                task = db.session.query(Task).filter(Task.id == task_id).first()
                return task
        
        @staticmethod  
        def delete_task_repo(task_id):
                task = Task.query.get(task_id)
                db.session.delete(task)
                return task
        
        @staticmethod  
        def get_all_task_repo():
                return Task.query.all()

        @staticmethod
        def task_with_no_resource_repo():
                tasks = db.session.query(Task).outerjoin(ResourceAllocation, Task.id == ResourceAllocation.task_id).filter(ResourceAllocation.resource_id.is_(None)).all()
                return tasks
        
        @staticmethod  
        def add_task_repo(args):
                new_task = Task(**args)
                db.session.add(new_task)
                return new_task
        
        
        
        @staticmethod
        def add_new_task_repo(args, resource_id):
                """create new task and allocation"""
                try:
                        task_data = {
                        "task_name": args.get('task_name'),
                        "start_date": args.get('start_date'),
                        "end_date": args.get('end_date'),
                        "description": args.get('description')
                        }
                        new_task = Task(**task_data)

                        allocation = ResourceAllocation(
                                resource_id=resource_id,
                                allocation_date=datetime.now(),
                                taskss = new_task
                        )
                        new_task.Resource_Allocation.append(allocation)
                        db.session.add(new_task)

                        return new_task
                
                except Exception as e:
                        db.session.rollback()
                        return jsonify({'error': str(e)}), 500
 

