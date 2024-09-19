from app import db
from models.Image_model import ResourceImage
from models.Resoucre_model import Resource
from marshmallow import ValidationError
from io import BytesIO
from flask import send_file


class image_repo:
    @staticmethod
    def upload_image_repo(image, resource_id):
        resource = Resource.query.filter_by(resource_id=resource_id).first()
        if not resource:
            raise ValidationError("Resource does not exist") #Return error if resource not found

        new_image = ResourceImage(resource_id=resource_id, image_data=image.read())
        db.session.add(new_image)
        return "Image saved successfully"


    @staticmethod
    def check_image(resource_id):
        resource = ResourceImage.query.filter_by(resource_id = resource_id).first()
        return resource
    
    @staticmethod
    def get_image_repo(resource_id):
        # Fetch the image based on resource_id
        image_record = ResourceImage.query.filter_by(resource_id=resource_id).first()
        if image_record:
            # return image_record.image_data  # Return binary image data
            return send_file(BytesIO(image_record.image_data), mimetype='image/jpeg', as_attachment=False)
        return None
    
    @staticmethod
    def update_image_repo(image, resource_id):

        # Check if an image already exists for the resource
        existing_image = ResourceImage.query.filter_by(resource_id=resource_id).first()
        existing_image.image_data = image.read()
        
        return "Image updated successfully"
