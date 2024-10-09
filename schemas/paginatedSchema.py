from marshmallow import Schema, fields
from schemas.ProjectSchema import ProjectSchema


class ProjectPaginationSchema(Schema):
    projects = fields.List(fields.Nested(ProjectSchema))  
    
    page = fields.Int()
    limit = fields.Int()
    total_projects = fields.Int(attribute="total")
    total_pages = fields.Int(attribute="pages")