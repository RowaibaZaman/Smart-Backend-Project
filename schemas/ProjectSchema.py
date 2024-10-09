

from models.project_model import Project
from app import ma
from schemas.TaskSchema import TaskSchema
from datetime import datetime
from schemas.ResourceAllocationSchema import ResourceAllocationSchema
from marshmallow import pre_load


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Project
        include_relationships = True
        load_instance = True
        include_fk = True
        
    tasks = ma.Nested(TaskSchema,many = True, only=['task_name', 'id', 'description','Resource_Allocation'])
    resource_allocation = ma.Nested(
        ResourceAllocationSchema, many=True, only=['resource.resource_name']
    )

    @pre_load
    def conversion(self, data, **kwargs):
        if 'start_date' in data and data['start_date']:
            data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
        if 'end_date' in data and data['end_date']:
            data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')


