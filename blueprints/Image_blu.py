from flask import Blueprint, jsonify
from webargs import fields
from marshmallow import ValidationError
from webargs.flaskparser import use_args
from bl.image_bl import Image_bl
from models.Resoucre_model import Resource

# Create the blueprint
image_bp = Blueprint('images', __name__)

#UPLOAD ROUTE

@image_bp.route('/upload_image', methods=['POST'])
@use_args({
    "resource_id": fields.Int(required=True),
}, 
location ="form")

def upload_image(args):
    """ upload image in db if resource exists"""

    resource_id = args.get('resource_id')
    image = request.files.get('image_data')

   # debug statements to check the incoming data
    # print(f"Resource ID: {resource_id}")
    # print(f"Image Object: {image}")

    if not image:
            raise ValidationError("No image file provided")
    try:
        
        image_data = Image_bl.upload_image_bl(resource_id, image)
        return jsonify({'message': image_data}), 200

    except ValidationError as e:
        return jsonify({'error': str(e)}), 400


# GET route 

@image_bp.route('/get_image', methods=['GET'])
@use_args({
    'resource_id': fields.Int(required=True)
}, location="query")  

def get_image(args):
    """ Return uteh image of resource"""
    resource_id = args.get('resource_id')
    try:
       
        image_data = Image_bl.get_image_bl(resource_id)
        
        return image_data
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400



# UPDATE ROUTE

@image_bp.route('/update_image', methods = ['PUT'])
@use_args({
    'resource_id': fields.Int(required= True) 
}, location = 'form')

def update_image_blu(args):
    """ Update the image 
    take resource id and image
    chek if image exist then update"""

    resource_id = args.get('resource_id')
    image = request.files['image_data']

    try:
        image_data = Image_bl.update_image_bl(image, resource_id)
        return jsonify({'message': image_data}), 200
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    

# @image_bp.route('/test_resource', methods=['GET'])
# def test_resource():
#         """ a test function to chk resource exists"""
#         resource_id = 3  
#         resource = Resource.query.filter_by(resource_id=resource_id).first()
#         return jsonify({'resource_found': bool(resource)})

