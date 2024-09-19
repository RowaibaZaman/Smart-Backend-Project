
from app import ma
from models.Resourcealloctaion_model import ResourceAllocation
from schemas.ResourceSchema import ResourceSchema
# from schemas.ProjectSchema import ProjectSchema
from datetime import datetime
from marshmallow import pre_load



class ResourceAllocationSchema(ma.SQLAlchemyAutoSchema):

    
    class Meta:
        model = ResourceAllocation

        include_fk = True
        load_instance = True

    resource = ma.Nested(ResourceSchema) 
    
    @pre_load
    def conversion(self, data, **kwargs):
        if 'allocation_date' in data and data['allocation_date']:
            data['allocation_date'] = datetime.strptime(data['allocation_date'], '%Y-%m-%d')
