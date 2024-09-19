from repository.image_repo import image_repo
from marshmallow import ValidationError
from repository.resource_repo import Resource_repo
from app import db

class Image_bl:

    @staticmethod
    def upload_image_bl(image, resource_id):
        image = image_repo.check_image(resource_id)
        if image:
            raise ValidationError("Image already uploaded")

        image_data = image_repo.upload_image_repo(image, resource_id)

        db.session.commit()
        return image_data

    
    
    @staticmethod
    def get_image_bl(resource_id):  
        return image_repo.get_image_repo(resource_id)
    
    @staticmethod
    def update_image_bl(image, resource_id):

        check_resource = image_repo.check_image(resource_id)
        if not check_resource:
            raise ValidationError("Reource Image Doesn't Exists")

        # No need to explicitly check resource existence here, it's done in the repo layer
        image_data = image_repo.update_image_repo(image, resource_id)
        # Commit the changes to the database
        db.session.commit()
        return image_data