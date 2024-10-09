from models.task_model import Task
from app import ma
from marshmallow import pre_dump, pre_load, post_dump,ValidationError
from schemas.ResourceAllocationSchema import ResourceAllocationSchema
from datetime import datetime


class TaskSchema(ma.SQLAlchemyAutoSchema):
    Resource_Allocation = ma.Nested(
        ResourceAllocationSchema, many=True, only=['resource.resource_name']
    )

    class Meta:
        model = Task
        load_instance= True
        include_fk = True
        
    
    @pre_load
    def conversion(self, data, **kwargs):
        if 'start_date' in data and data['start_date']:
            data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
        if 'end_date' in data and data['end_date']:
            data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')


        
    @pre_load
    def capitalize_task_name(self, data, **kwargs):

        if 'task_name' not in data or not data['task_name']:
            raise ValidationError("Task name is required.")
        return data
        

    @pre_dump
    def capitalize_task_name(self, data, **kwargs):
        data.task_name = data.task_name.upper()
        return data
    
    @post_dump
    def format_task_name(self, data, **kwargs):
        if 'task_name' in data:
            data['task_name'] = data['task_name'].title()  
        return data
    
