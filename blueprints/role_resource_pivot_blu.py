from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import ValidationError
from bl.role_resource_pvt_bl import role_resource_BL

role_resource_bp = Blueprint('role_resource', __name__)

@role_resource_bp.route('/add_role_resource', methods=['POST'])
@use_args({
    "resource_id": fields.Int(required=True),  
    "role_id": fields.Int(required=True)  
}, location='json')
def assign_role(args):
    """ 
    Assign a role to a resource.

    This endpoint allows assigning a specified role to a resource in the system.
    It ensures that the provided resource and role IDs are valid and performs the assignment.

    Args:
        resource_id (int): The ID of the resource to which the role will be assigned.
        role_id (int): The ID of the role to be assigned to the resource.

    Returns:
        JSON response containing success message or error message.
    """

    resource_id = args.get('resource_id') 
    role_id = args.get('role_id') 

    try:
        result = role_resource_BL.assign_role_to_resource(resource_id, role_id)
        if result:  # Assuming result is True on success
            return jsonify({"message": "Role assigned successfully!"}), 200
        else:
            return jsonify({"error": "Failed to assign role. Check resource and role IDs."}), 400

    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
