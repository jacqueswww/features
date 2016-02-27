from flask import Blueprint, jsonify
from flask import request


from users.services.user_services import UserServices


users = Blueprint('users', __name__)


@users.route('/login', methods=['POST'])
def users_endpoint():
    print('WWWWWWWWWWWot')
    print(request)
    print(request.method)
    if request.method == 'POST':
        params = request.get_json()

        if all(pkey in params for pkey in ("user", "password")):  # must have user and password keys.
            res = UserServices.login(
                username=params.get("user"),
                password=params.get("password")
                )

            if res:
                return jsonify({'message': 'You are logged in now.'}), 200
            else:
                return jsonify({'message': 'Login failed.'}), 401

    return jsonify({'message': 'Misunderstood'}), 400
