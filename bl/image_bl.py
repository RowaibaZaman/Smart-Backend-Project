from repository.image_repo import image_repo
from marshmallow import ValidationError
from repository.resource_repo import Resource_repo
from app import db

class Image_bl:

    @staticmethod
    def upload_image_bl( resource_id, image):

        resource_check = Resource_repo.check_resource_id(resource_id)
        if not resource_check:
            raise ValidationError("Resource doesn't exists")
        
        imagecheck = image_repo.check_image(resource_id)
        if imagecheck:
            raise ValidationError("Image already uploaded")
        
        image_data = image_repo.upload_image_repo( resource_id, image)

        db.session.commit()
        return image_data

    
    
    @staticmethod
    def get_image_bl(resource_id):  
        image =  image_repo.get_image_repo(resource_id)
        if not image:
            raise ValidationError("Image for this resource doesn't exist")
        return image
    
    
    @staticmethod
    def update_image_bl(image, resource_id):

        check_resource = image_repo.check_image(resource_id)
        if not check_resource:
            raise ValidationError("Reource Image Doesn't Exists")

        
        image_data = image_repo.update_image_repo(image, check_resource)

        # Commit the changes to the database
        db.session.commit()
        return image_data