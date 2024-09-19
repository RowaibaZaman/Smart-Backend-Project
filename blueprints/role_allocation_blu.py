from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from bl.role_allocation_bl import RoleAllocation_BL
from marshmallow import ValidationError
 
roleAllocation_bp = Blueprint('RoleAllocation', __name__)

@roleAllocation_bp.route('/add_role_allocation', methods= ['POST'])
@use_args({
    "resource_id": fields.Int(required= True),
    "role_id": fields.Int(required= True),
}, location = 'json')


def add_resourceAllocation(args):

    # resource_id = args.get("resource_id")
    # role_id = args.get("role_id")
    try:
        
        new_allocation = RoleAllocation_BL.add_role_allocation_bl(args)
        return jsonify(new_allocation), 201 
    
    except Exception as e:
        return jsonify({'message': f"An unexpected error occurred: {str(e)}"}), 500
    


@roleAllocation_bp.route('/delete_role_allocation', methods = ['DELETE'])
@use_args({
    "role_allocation_id": fields.Int(required= True)
}, location = 'query')

def delete_role_allocation(args):
    try:
        id = args.get('role_allocation_id')
        result = RoleAllocation_BL.delete_role_allocation_bl(id)
        return jsonify(result), 200
    
    except ValidationError as ve:
            # Handle the validation error and return a 404 if the role allocation doesn't exist
            return jsonify({"message": str(ve)}), 404


@roleAllocation_bp.route('/get_role', methods= ['GET'])
@use_args({
     "resource_id": fields.Int(required= True)

}, location = 'query')

def return_role(args):
    try:
        id = args.get('resource_id')
        result = RoleAllocation_BL.return_role_bl(id)
        return result
    except ValidationError as ve:
            return jsonify({"message": str(ve)}), 404

@roleAllocation_bp.route('/get_all_role', methods= ['GET'])

def all_roles():
    try:
         result = RoleAllocation_BL.all_role_bl()
         return result
    except ValidationError as ve:
         return jsonify({"message": str(ve)}), 404


          