
# from flask import Blueprint, jsonify, request
# from webargs import fields
# from webargs.flaskparser import use_args
# from bl.resourceallocation_bl import Allocation_BL
# from marshmallow import ValidationError
# import traceback

 
# resourceAllocation_bp = Blueprint('resourceAllocation', __name__)

# # @resourceAllocation_bp.route('/add_resource_allocation', methods = ['POST'])
# # @use_args({
# #     "resource_id": fields.Int(required= True),
# #     "task_id": fields.Int(required= False),
# #     "allocation_date": fields.Date( required = True),
# #     "project_id": fields.Int(required= False)
# # }, location = 'json')


# # def add_resourceAllocation(args):
# #     try:
# #         print("Received arguments:", args)

# #         new_allocation = Allocation_BL.add_resouceAllocation_bl(args)
# #         return jsonify(new_allocation)
# #     except ValidationError as ve:
# #         # Print validation errors
# #         print(f"ValidationError: {ve.messages}")
# #         return jsonify({"error": ve.messages}), 422
    
# #     except Exception as e:
# #         # Handle any other unexpected exceptions
# #         traceback.print_exc()

# #         return jsonify({'message': f"An unexpected error occurred: {str(e)}"}), 500


# #resource with task
# @resourceAllocation_bp.route('/resourceAllocation_with_task', methods= ['GET'])
# @use_args({
#     'id': fields.Int(required=True)
# }, location = 'query')
# def resource_with_task(args):

#     try:
        
#         result = Allocation_BL.resource_with_task_bl(args)
#         return result
#     except ValidationError as ve:
#         # Handle data validation errors
#         return jsonify({'message': str(ve)}), 400
#     except Exception as e:
#         # Handle other unexpected errors
#         return jsonify({'message': f"An unexpected error occurred: {str(e)}"}), 500



# # delete Allocation
# @resourceAllocation_bp.route('/delete_allocation', methods = ['DELETE'])
# @use_args({
#     "id": fields.Int(reuqired= True)
# }, location = 'query')

# def delete_repo(args):
#     id = args.get('id')
#     try:
#             result= Allocation_BL.delete_bl(id)
#             return result
    
#     except ValidationError as ve:
#         # Handle data validation errors from bl
#         return jsonify({'message': str(ve)}), 400
    
#     except Exception as e:
#             return jsonify({"message": f"An unexpected error occurred: {str(e)}"}), 500



# #get resource alllocation 
# @resourceAllocation_bp.route('/get_resource_allocation', methods = ["GET"])
# @use_args({
#       "id": fields.Int(required= True)
# }, location= 'query')

# def get_ra(args):
#       id = args.get('id')
#       result = Allocation_BL.get_resourceAllocation_BL(id)
#       return jsonify(result)


# @resourceAllocation_bp.route('/add_resource_allocations', methods=['POST'])
# def add_resourceAllocation():
#     try:
#         print("blueprints")


#         # Get JSON data from the request
#         data = request.get_json()

#         # Validate the incoming data
#         resource_id = data.get('resource_id')
#         allocation_date = data.get('allocation_date')
#         task_id = data.get('task_id')
#         project_id = data.get('project_id')

#         # Perform your own validation if necessary
#         if resource_id is None:
#             return jsonify({"error": "resource_id is required"}), 422
#         if allocation_date is None:
#             return jsonify({"error": "allocation_date is required"}), 422

#         # Prepare args dictionary to pass to the business logic layer
#         args = {
#             "resource_id": resource_id,
#             "allocation_date": allocation_date,
#             "task_id": task_id,
#             "project_id": project_id
#         }

#         print("Received arguments:", args)

#         # Call the business logic layer
#         new_allocation = Allocation_BL.add_resourceAllocation_bl(args)

#         return jsonify(new_allocation), 201  # Return 201 Created status
#     except ValidationError as ve:
#         # Print validation errors
#         print(f"ValidationError: {ve.messages}")
#         return jsonify({"error": ve.messages}), 422  # Return 422 Unprocessable Entity
#     except Exception as e:
#         # Handle any other unexpected exceptions
#         traceback.print_exc()
#         return jsonify({'message': f"An unexpected error occurred: {str(e)}"}), 500  # Return 500 Internal Server Error