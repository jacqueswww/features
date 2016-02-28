from features.models.feature import Feature
from features_app.db import db


class FeatureQueries:

    def _set_join_options():
        # sqlalchemy equivalent of an selected_related :-)
        res = Feature.query.options(db.joinedload(Feature.created_by))
        res = res.options(db.joinedload(Feature.client))
        res = res.options(db.joinedload(Feature.product_area))

        return res
    @classmethod
    def get_all(cls, queried_by):
        res = cls._set_join_options()
        res = res.order_by('client_id', 'client_priority')

        if queried_by.is_super:  # super users see everything.
            res = res.all()
        else:
            res = res.filter_by(created_by_id=queried_by.id)

        return res

    @classmethod
    def get_by_id(cls, _id, queried_by):
        res = cls._set_join_options()

        if queried_by.is_super:
            res = Feature.query.get(_id)
        else:
            res = Feature.query.filter_by(created_by_id=queried_by, id=_id)[0]

        return res

    @classmethod
    def get_all_by_client(cls, client, order_by_client_priority=False):
        res = cls._set_join_options()

        res = Feature.query.filter_by(client_id=client.id)

        if order_by_client_priority:
            res.order_by(Feature.client_priority)

        return res

    @staticmethod
    def get_max_client_priority_client(client):
        """
        Returns the highest current client priority.
        """

        res = db.session.query(db.func.max(Feature.client_priority)).filter_by(client_id=client.id).first()
        if not res[0]:
            return 0

        print('max_client_prioriyt => ' + str(res[0]))

        return res[0]

    @staticmethod
    def get_by_client_priority_subset(client, start_position, end_position):
        """
        On ordered set of client priorities return all features from give position in list.
        e.g.
            if client priority list is orderd by priority 0 .. n
            [start_position, end_position] will be returned.
        """

        res = Feature.query.filter_by(
                client_id=client.id
            ).filter(
                Feature.client_priority >= start_position
            ).filter(
                Feature.client_priority <= end_position
            )

        return res
