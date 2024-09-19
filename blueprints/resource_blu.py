
from flask import Blueprint,  jsonify
from webargs import fields
from webargs.flaskparser import use_args
from bl.resource_bl import ResourceBL
from marshmallow import  fields

    
resource_bp = Blueprint('resource', __name__)

#add resource
@resource_bp.route('/add_resource', methods=['POST'])
@use_args({
    "resource_name": fields.Str(required=True),
    "dep_id": fields.Int(required=True)

}, location='json')

def add_resource_route(args):
    result = ResourceBL.add_resource(args)
    return jsonify(result), 201




#get resource
@resource_bp.route('/get_resource', methods=['GET'])
@use_args(
    {
        "resource_id": fields.Int(required=True),
    }, location="query")
    
def get_route(args):
    resource_id = args.get('resource_id')
    result = ResourceBL.get_resource(resource_id)
    return jsonify(result)


@resource_bp.route('/get_all_resources', methods = ['GET'])
def get_all_resources():
    result = ResourceBL.get_all_resources()
    return result

@resource_bp.route('/delete_resource', methods = ["DELETE"])
@use_args({
    "resource_id": fields.Int(required = True)}, 
    location = 'query'
)
def delete_task(args):
    resource_id = args.get('resource_id')
    print(f"Received id: {resource_id}")
    result = ResourceBL.delete_resource_bl(resource_id)
    return jsonify(result)


@resource_bp.route('/resource_profile', methods= ['GET'])
@use_args({
    "resource_id": fields.Int(required=True),
    }, location="query")

def get_profile(args):
    resource_id = args.get('resource_id')
    result = ResourceBL.get_profile_BL(resource_id)
    return jsonify(result)