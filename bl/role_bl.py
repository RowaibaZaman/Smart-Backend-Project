from flask import jsonify
from app import db
from repository.role_repo import Role_repo 


class RoleBL:

    @staticmethod
    def add_role_bl(args):
        if not args:
            return {'message': 'No data entered'}, 400

        existing_role = Role_repo.check_role_exists(args.get("role_name"))
        if existing_role:
            return {"message": "Role with this name already exists"}, 400

        try:
            new_role = Role_repo.add_Role_repo(args)
            db.session.commit()

            # Serialize the new role using RoleSchema
            schema = Role_repo.get_role_schema()
            role_data = schema.dump(new_role)

            return {'message': 'New role added successfully', 'role': role_data}, 201

        except Exception as e:
            return {'message': f"An error occurred: {str(e)}"}, 500