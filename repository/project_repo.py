
# from datetime import datetime

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
        def get_project_schema(single=True):
                """Create and return the ProjectSchema instance."""
                return ProjectSchema() if single else ProjectSchema(many=True)
                