
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    ## Import and register blueprints
    from blueprints.dept_blu import department_bp
    from blueprints.project_blu import project_bp 
    from blueprints.task_blu import task_bp 
    from blueprints.resource_blu import resource_bp
    from blueprints.resourceallocation_blu import resourceAllocation_bp 
    from blueprints.role_blu import role_bp
    from blueprints.Image_blu import image_bp
    from blueprints.role_allocation_blu import roleAllocation_bp

    app.register_blueprint(department_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(resourceAllocation_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(roleAllocation_bp)
     

    
    return app

