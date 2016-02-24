from flask import Blueprint, jsonify


product_areas = Blueprint('product_areas', __name__)


@product_areas.route('/', methods=['GET'])
def product_areas_endpoint():
    return jsonify({
            "product_areas": [
                'Policies',
                'Billing',
                'Claims',
                'Reports'
            ]
        })
