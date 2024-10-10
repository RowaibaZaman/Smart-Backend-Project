from repository.resourceallocation_repo import Resource_Allocation_Repo 
from repository.resource_repo import Resource_repo
from repository.task_repo import Task_repo
from app import db
from flask import jsonify
from marshmallow import ValidationError
from repository.project_repo import Project_repo

class Allocation_BL:
    @staticmethod
    def delete_bl(id):
            result = Resource_Allocation_Repo.del_repo(id)
            if result:
                db.session.commit()
                return {"message": "allocation deleted sucessufully"}, 200
            else:
                print("Resource allocation not found")
                raise ValidationError("Resource allocation not found.")
        
    @staticmethod
    def add_resouceAllocation_bl(args):
            resource_id = args.get('resource_id')
            task_id = args.get('task_id')
            project_id = args.get('project_id')

            if Resource_Allocation_Repo.check_resource_allocation(resource_id, task_id):
                raise ValidationError("Resource allocation already exists.")
            
            check = Resource_repo.check_resource_id(resource_id)
            if not check:
                raise ValidationError("Resource id doesn't exists")
            if task_id:
                task_check = Task_repo.check_task_id(task_id)
                if not task_check:
                    raise ValidationError("Task id doesn't exists")
                
            if project_id:
                project_check = Project_repo.check_project(project_id)
                if not project_check:
                    raise ValidationError("Project doesn't exists ")

            new_ra = Resource_Allocation_Repo.add_allocation_repo(args)
            db.session.commit()

            schema =  Resource_Allocation_Repo.get_resourceAllocation_schema()
            serialized_data = schema.dump(new_ra)
            print("Serialized data:", serialized_data)
            return {'message': "ResourceAllocation added successfully"}, 201
    
    
    @staticmethod
    def resource_with_task_bl(args):
        r_id = args.get('id')
        check = Resource_repo.check_resource_id(r_id)
        if not check:
                raise ValidationError("Resource id doesn't exists")
        
        resource_task = Resource_Allocation_Repo.resource_with_task_repo(r_id)
        if resource_task:
            task_schema = Task_repo.get_task_schema(single = False)
                
            serialized_tasks = task_schema.dump(resource_task)
              
            return jsonify(serialized_tasks)
        else:
            raise ValidationError("allocation doesn't exists")
            
    @staticmethod
    def get_resourceAllocation_BL(id):
        ra = Resource_Allocation_Repo.get_ra_repo(id)
        if ra:

            schema = Resource_Allocation_Repo.get_resourceAllocation_schema()  
            result = schema.dump(ra)
            return result
        else:
            raise ValidationError("Resource Allocation not found")
        

        