from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from bl.role_bl import RoleBL


role_bp = Blueprint('role', __name__)

#addd role
@role_bp.route('/add_role', methods=['POST'])
@use_args({
    "role_name": fields.Str(required=True)
}, location='json')
def add_role(args):
    role = RoleBL.add_role_bl(args)
    return jsonify(role)


