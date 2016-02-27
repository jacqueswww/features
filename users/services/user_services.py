from flask.ext.login import login_user
from werkzeug.security import check_password_hash

from users.services.user_queries import UserQueries


class UserServices:

    def login(username, password):
        user = UserQueries.get_by_login(username)

        if user is not None:  # cool, we found a user.
            if check_password_hash(user.password, password):  # does the password match.
                return True
        else:
            check_password_hash(password, password)  # Say no timing attacks.

        return False
