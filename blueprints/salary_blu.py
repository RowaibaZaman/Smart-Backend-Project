from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from webargs import fields
from bl.salary_bl import SalaryBL
from models.salary_model import Salary
from models.Resoucre_model import Resource
from marshmallow import ValidationError


salary_bp = Blueprint('salary_bp', __name__)


@salary_bp.route('/add_salary', methods=['POST'])
@use_args({
    "resource_id": fields.String(required = True),
    "salary": fields.Decimal(required = True)
}, location='json')

def add_salary(args):
    resource_id = args.get('resource_id')
    salary_amount = args.get('salary')
    
    try:
        response = SalaryBL.add_salary(args)
        return jsonify(response), 201
    
    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500