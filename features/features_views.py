from flask import Blueprint, jsonify
from flask import request
from flask.ext.login import current_user, login_required

from features.queries.feature_queries import FeatureQueries
from features.services.feature_services import FeatureServices
from features.serializers.feature_serializer import FeatureSerializer

features = Blueprint('features', __name__)


@features.route('/', methods=['GET', 'POST'])
@features.route('/<pk>/', methods=['GET', 'PATCH', 'DELETE'])
@login_required
def features_endpoint(pk=None):
    if request.method == 'GET':
        if pk:  # is query for single instance.
            feature = FeatureQueries.get_by_id(pk, queried_by=current_user)
            if feature:
                return jsonify(FeatureSerializer().dump(feature).data)
            else:
                return jsonify({'message': 'Feature not Found'}), 404

        else:    # is query for all instances.
            results = FeatureQueries.get_all(queried_by=current_user)
            return jsonify({
                "results": FeatureSerializer(many=True).dump(results).data
                })

    elif request.method == 'POST':
        params = request.get_json()
        feature = FeatureServices.create(params=params, action_by=current_user)

        return jsonify(FeatureSerializer().dump(feature).data)

    elif request.method == "DELETE":
        if pk:  # is query for single instance.
            feature = FeatureQueries.get_by_id(pk, queried_by=current_user)
            if feature:
                if FeatureServices.delete(feature, action_by=current_user):
                    return jsonify({'message': 'Done'}), 200
            else:
                return jsonify({'message': 'Feature not Found'}), 404
        
    elif request.method == 'PATCH':
        if pk:
            params = request.get_json()
            feature = FeatureQueries.get_by_id(pk, queried_by=current_user)
            if feature:
                feature = FeatureServices.update(feature, params=params, action_by=current_user)

                return jsonify(FeatureSerializer().dump(feature).data)
            else:
                return jsonify({'message': 'Feature not Found.'}), 404
        else:
                return jsonify({'message': 'Please provide a Feature ID to update.'}), 400

    return jsonify({'message': 'Misunderstood'}), 400
