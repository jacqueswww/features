from flask import Blueprint, jsonify


clients = Blueprint('clients', __name__)


@clients.route('/', methods=['GET'])
def clients_endpoint():
    return jsonify({
            "clients": [
                "Client A",
                "Client B",
                "Client C"
            ]
        })
