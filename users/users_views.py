from flask import Blueprint, jsonify
from flask import request
from flask.ext.login import current_user


from users.services.user_services import UserServices, UserServicesException


users = Blueprint('users', __name__)


@users.route('/login', methods=['POST'])
def users_endpoint():

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


@users.route('/register', methods=['POST'])
def users_register():

    if request.method == 'POST':
        params = request.get_json()

        if all(pkey in params for pkey in ("username", "password", "first_name", "last_name", "email")):  # must have user and password keys.
            try:
                res = UserServices.register(
                    params=params
                    )
            except UserServicesException as e:
                return jsonify({'message': str(e)}), 401

            if res:
                return jsonify({'message': 'You are registerd now.'}), 200
            else:
                return jsonify({'message': 'Registration failed.'}), 400
        else:
            jsonify({'message': 'Please fill in all fields.'}), 400

    return jsonify({'message': 'Misunderstood'}), 400


@users.route('/profile', methods=['GET'])
def users_profile():

    if not hasattr(current_user, 'is_super'):
        return jsonify({'message': 'Not logged in.'}), 401

    return jsonify({
        'is_super': current_user.is_super
        })
