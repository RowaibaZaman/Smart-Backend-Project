# from schemas.ResourceAllocationSchema import resourcesallocation_schema
from repository.resourceallocation_repo import Resource_Allocation_Repo 
from repository.resource_repo import Resource_repo
from repository.task_repo import Task_repo
from app import db
from flask import jsonify
from marshmallow import ValidationError

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
    def add_resouceA(args):
            resource_id = args.get('resource_id')
            task_id = args.get('task_id')

            if Resource_Allocation_Repo.check_resource_allocation(resource_id, task_id):
                raise ValidationError("Resource allocation already exists.")
            
            check = Resource_repo.check_resource_id(resource_id)
            if not check:
                raise ValidationError("Resource id doesn't exists")
            
            task_check = Task_repo.check_task_id(task_id)
            if not task_check:
                 raise ValidationError("Task id doesn't exists")

            new_ra = Resource_Allocation_Repo.add_allocation_repo(args)
            db.session.commit()

            schema =  Resource_Allocation_Repo.get_resourceAllocation_schema(single = False)

            serialized_data = schema.dump(new_ra)
            return {'message': "ResourceAllocation added successfully", 'resourcesallocation':serialized_data}, 201

    @staticmethod
    def resource_with_task_bl(args):
        r_id = args.get('id')
        resource = Resource_Allocation_Repo.resource_with_task_repo(r_id)
        if resource:
            return jsonify(resource)
        else:
            raise ValidationError("resource_id doesn't exists")
            
    @staticmethod
    def get_resourceA_BL(id):
        ra = Resource_Allocation_Repo.get_ra_repo(id)
        if ra:

            schema = Resource_Allocation_Repo.get_resourceAllocation_schema()  
            result = schema.dump(ra)
            return result
        else:
            raise ValidationError("Resource Allocation not found")
        

        