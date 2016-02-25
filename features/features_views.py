from flask import Blueprint, jsonify
from flask import request
from flask.ext.login import current_user

from features.queries.feature_queries import FeatureQueries
from features.services.feature_services import FeatureServices
from features.serializers.feature_serializer import FeatureSerializer


features = Blueprint('features', __name__)


@features.route('/', methods=['GET'])
@features.route('/<pk>/', methods=['GET'])
def features_endpoint(pk=None):
    if request.method == 'GET':
        if pk:
            feature = FeatureQueries.get_by_id(pk)
            print(feature)
            print('ddddd')
            if feature:
                return jsonify(FeatureSerializer().dump(feature).data)
            else:
                return jsonify({'message': 'Feature not Found'}), 404

        else: # is list all query.
            results = FeatureQueries.get_all()

            return jsonify(FeatureSerializer(many=True).dump(results).data)

    if request.method == 'POST':
        params = request.get_json()
        feature = FeatureServices.create(params=params, action_by=current_user)

        return jsonify(FeatureSerializer().dump(feature).data)        

    return jsonify({'message': 'Misunderstood'}), 400
