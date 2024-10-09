from app import ma
from models.Resoucre_model import Resource
from marshmallow import post_dump
class ResourceSchema(ma.SQLAlchemyAutoSchema):    
    class Meta:
        model = Resource
        include_fk = True
        include_relationship = True
        load_instance = True

    @post_dump
    def remove_empty_resource_allocation(self, data, **kwargs):
        if 'resource_allocation' in data and not data['resource_allocation']:
            del data['resource_allocation']
        return data
    
  