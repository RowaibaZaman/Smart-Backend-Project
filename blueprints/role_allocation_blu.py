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

    """ This blueprint assigns the resource a role, take input of of role_id and resource_id"""

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

    """ This blueprint if to delet the allocation
    Take the resource_allocation Id in input """

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
    """This blueprint retrun the role of resoruce return the role associate with the id"""
    

    try:
        
        id = args.get('resource_id')
        result = RoleAllocation_BL.return_role_bl(id)
        return result
    except ValidationError as ve:
            return jsonify({"message": str(ve)}), 404





@roleAllocation_bp.route('/get_all_role', methods= ['GET'])

def all_roles():

    """Return all the roleallocation inclue role, resource_name and role allocation id """
    try:
         result = RoleAllocation_BL.all_role_bl()
         return result
    except ValidationError as ve:
         return jsonify({"message": str(ve)}), 404



@roleAllocation_bp.route('/assign_role', methods=['POST'])
@use_args({
    "assigner_resource_id": fields.Int(required=True),  
    "assignee_resource_id": fields.Int(required=True),  
    "role_id": fields.Int(required=True)  
}, location='json')
def assign_role(args):
    
    """ This blueprint Assign role, but first check if assigner is Manager 
        Then role is assigned by manager to other resources"""

    assigner_resource_id = args.get('assigner_resource_id') 
    assignee_resource_id = args.get('assignee_resource_id') 
    role_id = args.get('role_id') 

    try:
        
        result = RoleAllocation_BL.assign_role_to_resource(assigner_resource_id, assignee_resource_id, role_id)
        return jsonify(result), 200

    except ValidationError as e:
        return jsonify({str(e.messages)}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
          