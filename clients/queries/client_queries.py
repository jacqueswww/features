from clients.models.client import Client


class ClientQueries:

    def get_all():
        res = Client.query.all()

        return res

    def get_by_id(_id):

        res = Client.query.get(_id)

        return res
