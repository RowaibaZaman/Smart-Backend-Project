from repository.image_repo import image_repo
from app import db

class Image_bl:

    @staticmethod
    def upload_image_bl(image, resource_id):
        
        image_data = image_repo.upload_image_repo(image, resource_id)

        db.session.commit()
        return image_data
    
    @staticmethod
    def get_image_bl(resource_id):  
        return image_repo.get_image_repo(resource_id)