
from app import db
from datetime import datetime
from flask import jsonify
from repository.project_repo import Project_repo
# from schemas.ProjectSchema import project_schema, projects_schema
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

            result = [{
                "project_id": project.project_id,
                "project_name": project.project_name,
                "start_date": project.start_date.strftime('%Y-%m-%d'),
                "end_date": project.end_date.strftime('%Y-%m-%d'),
                "description": project.description
            }
            for project in projects]
            return  result
      
            
    @staticmethod
    def project_with_task_bl(project_id):
        try:
            project = Project_repo.project_with_task_repo(project_id)
            if not project:
                return {"message": "Project not found"}, 404
            
            # result = project_schema.dump(project)
            schema = Project_repo.get_project_schema()  # Get the single schema
            result = schema.dump(project)
            return result
            

        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500
        
