
from app import db
from repository.project_repo import Project_repo
from flask import jsonify
from repository.resource_repo import Resource_repo
from marshmallow import ValidationError
class Project_BL:
    @staticmethod
    def add_project_bl(args):
        try:
            new_project = Project_repo.add_project_repo(args)

            
            db.session.commit()
            return{"message": "New Project added", 'project': new_project}
        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500
        
    @staticmethod
    def get_project_bl():
            
            projects = Project_repo.get_all_projects()

            schema = Project_repo.get_project_schema(single = False)  # Get the single schema
            result = schema.dump(projects)
            return  result
      
            
    @staticmethod
    def project_with_task_bl(project_id):
        try:
            project = Project_repo.project_with_task_repo(project_id)
            if not project:
                return {"message": "Project not found"}, 404

            schema = Project_repo.get_project_schema()  
            result = schema.dump(project)
            return result
            

        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500
        

    @staticmethod
    def update_project_bl(project_id, update_data):
        try:
            # Check if the project exists
            project = Project_repo.check_project(project_id)
            if not project:
                raise ValidationError(" Projectnot found")
               
            # If the project exists
            updated_project = Project_repo.update_project_repo(project_id, update_data)
            db.session.commit()

            schema = Project_repo.get_project_schema(single = True)
            result = schema.dump(updated_project)

            return {"message": "Project updated successfully", "project": result}
        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500
        

    @staticmethod
    def get_paginated_project_bl(args):
        """ Get paginated projects"""
        limit = args.get('limit')
        page = args.get('page')
        paginated_projects = Project_repo.get_paginated_projects_repo(limit, page)

        schema = Project_repo.get_project_schema(single = False)
        projects_result = schema.dump(paginated_projects)

        return{
            "project": projects_result,
            "total_projects": paginated_projects.total,
            "page_no": paginated_projects.page,
            "total_pages": paginated_projects.pages
        }
    
    
    @staticmethod
    def new_project_bl(args):
        """ adding new project and allocation"""
        resource_id = args.get('resource_id')
        #check resoruce
        if resource_id:
            resource = Resource_repo.check_resource_id
            if not resource:
                raise ValidationError("Resource not found")
                        
        project = Project_repo.add_new_project(args, resource_id )
        if project:
            db.session.commit()
        return jsonify({"message": "Project and Resource Allocation created successfully"}), 201
