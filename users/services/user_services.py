from flask.ext.login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from features_app.db import db
from features_app.utils import set_fields_from_dict, get_fields
from users.services.user_queries import UserQueries
from users.models.user import User


class UserServicesException(Exception):
    pass


class UserServices:

    def login(username, password):
        user = UserQueries.get_by_login(username)

        if user is not None:  # cool, we found a user.
            if check_password_hash(user.password, password):  # does the password match.
                login_user(user)
                return True
        else:
            check_password_hash(password, password)  # Say no timing attacks.

        return False

    def register(params, login=True, commit=True):
        """
        Create / register a user.
        """

        if  UserQueries.get_by_login(params.get("username", "")):
            raise UserServicesException('User with given username exists already.')

        user = User()
        model_fields = get_fields(User)

        # apply all fields to object.
        set_fields_from_dict(user, params, model_fields)

        user.login=params.get("username")
        user.password=generate_password_hash(params.get("password"))

        if commit:
            db.session.add(user)
            db.session.commit()
            
        if login:
            login_user(user)

        return user
