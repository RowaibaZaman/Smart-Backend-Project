
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

            # result = [{
            #     "project_id": project.project_id,
            #     "project_name": project.project_name,
            #     "start_date": project.start_date.strftime('%Y-%m-%d'),
            #     "end_date": project.end_date.strftime('%Y-%m-%d'),
            #     "description": project.description
            # }
            # for project in projects]

            schema = Project_repo.get_project_schema(single = False)  # Get the single schema
            result = schema.dump(projects)
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
        

    @staticmethod
    def update_project_bl(project_id, update_data):
        try:
            # Check if the project exists
            project = Project_repo.check_project(project_id)
            if not project:
                return {"message": "Project not found"}, 404
            
            # If the project exists
            updated_project = Project_repo.update_project_repo(project_id, update_data)
            db.session.commit()

            schema = Project_repo.get_project_schema(single = True)
            result = schema.dump(updated_project)

            return {"message": "Project updated successfully", "project": result}
        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500
        

    @staticmethod
    def get_paginated_projects_bl(limit, page):
        projects = Project_repo.get_paginated_projects(limit, page)
        total_count = Project_repo.get_total_project_count()

        schema = Project_repo.get_project_schema(single=False)
        result = schema.dump(projects)

        # Include pagination metadata
        return {
            "projects": result,
            # "total_projects": total_count,
            "page": page,
            "limit": limit,
            "total_pages": (total_count + limit - 1) // limit  # Total number of pages
        }
