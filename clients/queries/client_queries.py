from clients.models.client import Client


class ClientQueries:

    def get_all():
        res = Client.query.all()

        return res
