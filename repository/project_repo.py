

from models.project_model import Project
from models.task_model import Task
from models.Resourcealloctaion_model import ResourceAllocation
from app import db
from sqlalchemy.orm import joinedload
from schemas.ProjectSchema import ProjectSchema


class Project_repo:
        @staticmethod
        def add_project_repo(args):
                new_projects = Project(**args)
                db.session.add(new_projects)
                return new_projects
                
        @staticmethod
        def get_all_projects():
                result =  Project.query.all()
                return result
        

        @staticmethod
        def project_with_task_repo(project_id):
                project = (
                db.session.query(Project)
                .options(joinedload(Project.tasks)
                        .joinedload(Task.Resource_Allocation)
                        .joinedload(ResourceAllocation.resource)
                
                )
                .filter(Project.project_id == project_id)
                .first()
                )
                return project
        
        @staticmethod
        def check_project(project_id):
                result = Project.query.filter_by(project_id=project_id).first()
                return result
        
        @staticmethod
        def update_project_repo(project_id, update_data):
                project = Project.query.get(project_id)
                
                # Update the project's fields
                for key, value in update_data.items():
                        if hasattr(project, key):
                                setattr(project, key, value)
                return project
        

        @staticmethod
        def get_project_schema(single=True):
                """Create and return the ProjectSchema instance."""
                return ProjectSchema() if single else ProjectSchema(many=True)
        

        @staticmethod
        def get_paginated_projects(limit=2, page=1):
                # Calculate offset based on the page and limit
                offset = (page - 1) * limit  

                #offset determine where to start fetching rows when querying a database.
                #offset: Defines how many records (rows) to skip before starting to fetch. 

                # Query with limit and offset for pagination
                query = Project.query.offset(offset).limit(limit)

                result = query.all()
                return result

        @staticmethod
        def get_total_project_count():
                return Project.query.count()
