from flask import Blueprint, jsonify
from flask.ext.login import login_required

from product_areas.serializers.product_area_serializer import ProductAreaSerializer
from product_areas.queries.product_area_queries import ProductAreaQueries


product_areas = Blueprint('product_areas', __name__)


@product_areas.route('/', methods=['GET'])
@login_required
def product_areas_endpoint():
    results = ProductAreaQueries.get_all()

    return jsonify({
        "results": ProductAreaSerializer(many=True).dump(results).data
        })
