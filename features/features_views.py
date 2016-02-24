from flask import Blueprint, jsonify
# from flask import request, current_app


features = Blueprint('features', __name__)


@features.route('/', methods=['GET'])
def features_endpoint():
    return jsonify({
        "message": "hello world",
        "version": "0.0.1"
        })
