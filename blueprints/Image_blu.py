from flask import Blueprint, jsonify, request, send_file
from webargs import fields
from marshmallow import ValidationError
from webargs.flaskparser import use_args
from bl.image_bl import Image_bl
from io import BytesIO


# Create the blueprint
image_bp = Blueprint('images', __name__)

#UPLOAD ROUTE

@image_bp.route('/upload_image', methods=['POST'])
@use_args({
    "resource_id": fields.Int(required=True),
}, 
location ="form")

def upload_image(args):
    
    resource_id = args.get('resource_id')
    image = request.files['image_data']

    try:
        #
        image_data = Image_bl.upload_image_bl(image, resource_id)
        
        return jsonify({'message': image_data}), 200

    except ValidationError as e:
        return jsonify({'error': str(e)}), 400


# GET route 

@image_bp.route('/get_image', methods=['GET'])
@use_args({
    'resource_id': fields.Int(required=True)
}, location="query")  
def get_image(args):
    resource_id = args.get('resource_id')
    
    # Call the business logic function
    image_data = Image_bl.get_image_bl(resource_id)
    
    return image_data



# UPDATE ROUTE

@image_bp.route('/update_image', methods = ['POST'])
@use_args({
    'resource_id': fields.Int(required= True) 
}, location = 'form')

def update_image_blu(args):
    resource_id = args.get('resource_id')
    image = request.files['image_data']

    try:
        # Call the business logic layer to update the image
        image_data = Image_bl.update_image_bl(image, resource_id)
        return jsonify({'message': image_data}), 200
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400