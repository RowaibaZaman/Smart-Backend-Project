from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from webargs import fields
from bl.salary_bl import SalaryBL
from marshmallow import ValidationError


salary_bp = Blueprint('salary_bp', __name__)


@salary_bp.route('/add_salary', methods=['POST'])
@use_args({
    "resource_id": fields.String(required = True),
    "salary": fields.Decimal(required = True)
}, location='json')

def add_salary(args):
    try:
        response = SalaryBL.add_salary(args)
        return jsonify(response), 201
    
    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@salary_bp.route('/get_salry', methods = ['GET'])
def get_salary():
    try:
        response = SalaryBL.get_all_salaries()
        return jsonify(response), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@salary_bp.route('/update_salary', methods=['POST'])
@use_args({
    "resource_id": fields.String(required=True),
    "salary": fields.Decimal(required=True)
}, location='json')
def add_or_update_salary(args):
 

    try:
        response, status_code = SalaryBL.update_salary_bl(args)
        return jsonify(response), status_code
    
    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500