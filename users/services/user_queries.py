from users.models.user import User


class UserQueries:

    def get_by_login(login):

        res = User.query.filter_by(login=login).first()

        if res:
            return res
        else:
            return None
