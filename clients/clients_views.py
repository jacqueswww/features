from flask import Blueprint, jsonify
from flask.ext.login import login_required

from clients.queries.client_queries import ClientQueries
from clients.serializers.client_serializer import ClientSerializer


clients = Blueprint('clients', __name__)


@clients.route('/', methods=['GET'])
@login_required
def clients_endpoint():
    results = ClientQueries.get_all()
    print(results)
    
    return  jsonify({
        "results": ClientSerializer(many=True).dump(results).data
        })
