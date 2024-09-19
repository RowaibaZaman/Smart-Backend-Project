
from flask import Blueprint, request, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from bl.resourceallocation_bl import Allocation_BL
from marshmallow import ValidationError
 
resourceAllocation_bp = Blueprint('resourceAllocation', __name__)

@resourceAllocation_bp.route('/add_resource_allocation', methods = ['POST'])
@use_args({
    "resource_id": fields.Int(required= True),
    "task_id": fields.Int(required= True),
    "allocation_date": fields.Str( required = True)
}, location = 'json')


def add_resourceAllocation(args):
    try:
        
        new_allocation = Allocation_BL.add_resouceA(args)
        return jsonify(new_allocation)
    except Exception as e:
        # Handle any other unexpected exceptions
        return jsonify({'message': f"An unexpected error occurred: {str(e)}"}), 500


#resource with task
@resourceAllocation_bp.route('/resourceAllocation_with_task', methods= ['GET'])
@use_args({
    'id': fields.Int(required=True)
}, location = 'query')
def resource_with_task(args):

    try:
        
        result = Allocation_BL.resource_with_task_bl(args)
        return result
    except ValidationError as ve:
        # Handle data validation errors
        return jsonify({'message': str(ve)}), 400
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({'message': f"An unexpected error occurred: {str(e)}"}), 500



# delete Allocation
@resourceAllocation_bp.route('/delete_allocation', methods = ['DELETE'])
@use_args({
    "id": fields.Int(reuqired= True)
}, location = 'query')

def delete_repo(args):
    id = args.get('id')
    try:
            result= Allocation_BL.delete_bl(id)
            return result
    
    except ValidationError as ve:
        # Handle data validation errors from bl
        return jsonify({'message': str(ve)}), 400
    
    except Exception as e:
            return jsonify({"message": f"An unexpected error occurred: {str(e)}"}), 500



#get resource alllocation 
@resourceAllocation_bp.route('/get_resource_allocation', methods = ["GET"])
@use_args({
      "id": fields.Int(required= True)
}, location= 'query')

def get_ra(args):
      id = args.get('id')
      result = Allocation_BL.get_resourceA_BL(id)
      return jsonify(result)

