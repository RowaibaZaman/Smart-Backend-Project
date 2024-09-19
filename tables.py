# create_tables.py
from app import create_app, db
app = create_app()

with app.app_context():
   
    from models.role_allocation_model import RoleAllocation
    from models.Resoucre_model import Resource
    # from models.role_model import Role
    db.create_all()
    print("Tables created successfully")