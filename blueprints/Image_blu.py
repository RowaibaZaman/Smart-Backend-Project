from flask import Blueprint, jsonify, request, send_file
from webargs import fields
from webargs.flaskparser import use_args
from bl.image_bl import Image_bl
from io import BytesIO


# Create the blueprint
image_bp = Blueprint('images', __name__)


@image_bp.route('/upload_image', methods=['POST'])
@use_args({
    "resource_id": fields.Int(required=True),
    # "image_data": fields.Field(required=True)
}, 
location ="form")

def upload_image(args):
    
    resource_id = args['resource_id']

    image = request.files['image_data']
    # Call the business logic function
    image_data = Image_bl.upload_image_bl(image, resource_id)
    return jsonify({'message': image_data})



# GET route 
@image_bp.route('/get_image', methods=['GET'])
@use_args({
    'resource_id': fields.Int(required=True)
}, location="query")  
def get_image(args):
    resource_id = args['resource_id']
    
    # Call the business logic function
    image_data = Image_bl.get_image_bl(resource_id)
    
    return image_data