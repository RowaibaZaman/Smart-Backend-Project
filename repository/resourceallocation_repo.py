from app import db
from models.Resourcealloctaion_model import ResourceAllocation
from models.task_model import Task
from repository.task_repo import Task_repo
from schemas.ResourceAllocationSchema import ResourceAllocationSchema
from sqlalchemy.orm import joinedload

# Create class
class Resource_Allocation_Repo:

    @staticmethod
    def get_resourceAllocation_schema(single=True):
                """Create and return the schema instance."""
                return ResourceAllocationSchema() if single else ResourceAllocationSchema(many=True)


    @staticmethod
    def add_allocation_repo(args):
            new_ra = ResourceAllocation(**args)
            db.session.add(new_ra)

            return new_ra
        

    @staticmethod
    def check_resource_allocation(resource_id, task_id):
        return db.session.query(ResourceAllocation).filter_by(
            resource_id=resource_id,
            task_id=task_id,
        ).first() is not None
    
    @staticmethod   
    def resource_with_task_repo(resource_id):
            
                # Query the ResourceAllocation table for entries with the given resource_id
                # allocationss = (db.session.query(ResourceAllocation)
                #             .filter(ResourceAllocation.resource_id == resource_id)
                #             .all())
                # task_ids = [allocation.task_id for allocation in allocationss]
                
                # Query Task table for all tasks with the extracted task_ids
                #filter tasks where the id is in the task_ids list.
                # tasks = db.session.query(Task).filter(Task.id.in_(task_ids)).all()
                
                tasks = (db.session.query(Task)
                 .join(ResourceAllocation)
                 .filter(ResourceAllocation.resource_id == resource_id)
                 .all())
               
                return tasks
            
    @staticmethod
    def del_repo(id):
            result = ResourceAllocation.query.get(id)
            if result:
               db.session.delete(result)
               return True
            return False


    @staticmethod
    def get_ra_repo(id):
        result = ResourceAllocation.query.options(
            joinedload(ResourceAllocation.resource)  
        ).filter_by(id=id).first()

        return result
    
    



    


