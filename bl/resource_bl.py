

from flask import jsonify
from app import db
from repository.resource_repo import Resource_repo


class ResourceBL:
    @staticmethod
    def add_resource(args):
        if not args:
            return {'message': 'No data entered'}
        
        existing_resource = Resource_repo.check_resource_exists(args.get("resource_name"))
        if existing_resource:
            return {"message": "Resource with this name already exists"}, 400
        
        try:
            new_resource = Resource_repo.add_Resource(args)
            db.session.commit()

            if new_resource:

                schema = Resource_repo.get_resource_schema()  
                result = schema.dump(new_resource)
                return {'message': 'New resource added successfully', 'resource': result}
            else:
                return {'message': 'Failed to add resource'}
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    @staticmethod
    def get_profile_BL(resource_id):
        resource = Resource_repo.get_profile(resource_id)

        # If no resource is found, return None
        if not resource:
            return None

        # Serialize the resource data using the Marshmallow schema
        schema = Resource_repo.get_resource_schema(single= True)
        result = schema.dump(resource)

        return result
    

    @staticmethod
    def get_resource(resource_id):
        resource = Resource_repo.get_resource_by_id(resource_id)
        if resource:
            return {'resource_name': resource.resource_name, 'dep_id': resource.dep_id}
        else:
            return {'error': 'Resource not found'}, 404
        



    @staticmethod
    def get_all_resources():
        try:
            result = Resource_repo.get_all_resource()
            schema = Resource_repo.get_resource_schema(single=False)
            serialized_result = schema.dump(result)
            for allocation in serialized_result:
                 if 'resource_allocation' in allocation: 
                     del allocation['resource_allocation']

            return jsonify(serialized_result)
        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500
        
    
    @staticmethod
    def delete_resource_bl(resource_id):
        try:
            resource = Resource_repo.delete_resource_repo(resource_id)
            if resource:
                db.session.delete(resource)
                db.session.commit()
                return {"message": "Resource deleted successfully"}, 200
            else:
                return {"message": "Resource not found"}, 404
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500

