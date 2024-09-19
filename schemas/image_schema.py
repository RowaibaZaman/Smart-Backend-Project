
from models.Image_model import ResourceImage
from app import ma

class ImageSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = ResourceImage
        include_relationships = True
        load_instance = True
        include_fk = True
