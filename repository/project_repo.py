from models.project_model import Project
from models.task_model import Task
from models.Resourcealloctaion_model import ResourceAllocation
from schemas.ProjectSchema import ProjectSchema
from schemas.paginatedSchema import ProjectPaginationSchema
from app import db
from sqlalchemy.orm import joinedload
from flask import jsonify
from datetime import datetime 

class Project_repo:
        @staticmethod
        def get_project_schema(single=True):
                """Create and return the ProjectSchema instance."""
                return ProjectSchema() if single else ProjectSchema(many=True)

        @staticmethod
        def get_paginated_schema(single=True):
                """Create and return the Paginated ProjectSchema instance."""
                return ProjectPaginationSchema() if single else ProjectPaginationSchema(many=True)

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
                """Return Tasks, resource associated with the project"""
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
                """ check project"""
                result = Project.query.filter_by(project_id=project_id).first()
                return result
        
        @staticmethod
        def update_project_repo(project_id, update_data):
                """ takes input field and update project accordingly"""
                project = Project.query.get(project_id)
                # Update the project's fields
                for key, value in update_data.items():
                        if hasattr(project, key):
                                setattr(project, key, value)
                return project

        @staticmethod
        def get_paginated_projects_repo(limit=2, page=1):
                """ pagination 2 projects per page"""
                return Project.query.paginate(page = page, per_page = limit)
        
        # @staticmethod
        # def add_new_project(args, resource_id):
        #         """ create new project and resource allocation"""
        #         try:
        #                 project_data = {
        #                 "project_name": args.get('project_name'),
        #                 "start_date": args.get('start_date'),
        #                 "end_date": args.get('end_date'),
        #                 "description": args.get('description')
        #                 }
        #                 # Create the new Project object with fields
        #                 new_projects = Project(**project_data)
                        
        #                 # Create the ResourceAllocation and append to project's resource_allocation relationship
        #                 allocation = ResourceAllocation(
        #                         resource_id=resource_id,
        #                         allocation_date=datetime.now(),  # Current date for allocation
        #                         project=new_projects  # Use the project relationship to save the allocation
        #                 )
        #                 new_projects.resource_allocation.append(allocation)
        #                 db.session.add(new_projects)
        #                 return new_projects
                        
                
        #         except Exception as e:
        #                 db.session.rollback()
        #                 raise e
                

        @staticmethod
        def add_new_project(args, resource_ids):
                """ Create a new project and allocate multiple resources """
                try:
                        project_data = {
                        "project_name": args.get('project_name'),
                        "start_date": args.get('start_date'),
                        "end_date": args.get('end_date'),
                        "description": args.get('description')
                        }
                        
                        # Create the new Project
                        new_project = Project(**project_data)
                        
                        # iterating over list of resources to add multiple allocation for same project
                        allocations = [
                        ResourceAllocation(
                                resource_id=resource_id,
                                allocation_date=datetime.now(),
                                project=new_project  # project relationship to save the allocation
                        ) for resource_id in resource_ids
                        ]
                        
                        #extand allocation to the new project's resource_allocation relationship
                        #extand beacuse there are multiple resources
                        new_project.resource_allocation.extend(allocations)
                        
                        db.session.add(new_project)
                        return new_project
                
                except Exception as e:
                        db.session.rollback()
                        raise e

                                
