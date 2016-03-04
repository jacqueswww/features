from features.models.feature import Feature
from clients.models.client import Client
from features_app.db import db


class FeatureQueries:

    def _set_join_options():
        # sqlalchemy equivalent of an selected_related :-)
        # (prevents one million unecessary requests :-P)
        res = Feature.query.options(db.joinedload(Feature.created_by))
        res = res.options(db.joinedload(Feature.client))
        res = res.options(db.joinedload(Feature.product_area))

        return res
    @classmethod
    def get_all(cls, queried_by):
        print("queried_by")
        print(queried_by)
        print(type(queried_by))
        print("queried_by")
        res = cls._set_join_options()

        if queried_by.is_super:
            res = res.order_by('master_priority')
        else:
            res = res.order_by('client_id', 'client_priority')

        if queried_by.is_super:  # super users see everything.
            res = res.all()
        else:
            res = res.filter_by(created_by_id=queried_by.id)

        return res

    @classmethod
    def get_all_ordered_by_master_priority(cls):
        res = cls._set_join_options()
        res = res.order_by('master_priority')

        return res

    @classmethod
    def get_by_id(cls, _id, queried_by):
        res = cls._set_join_options()

        if queried_by.is_super:
            res = Feature.query.get(_id)
            return res
        else:
            res = Feature.query.filter_by(created_by_id=queried_by.id, id=_id).first()
            if res:
                return res
            else:
                return None

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

        # print('max_client_priority => ' + str(res[0]))

        return res[0]

    @staticmethod
    def get_max_master_priority():
        """
        Returns the highest current master priority.
        """

        res = db.session.query(db.func.max(Feature.master_priority)).first()
        if not res[0]:
            return 0

        return res[0]

    @staticmethod
    def get_by_priority_subset(start_position, end_position, feature_field, client=None):
        """
        On ordered set of client priorities return all features from give position in list.
        e.g.
            if client priority list is orderd by priority 0 .. n
            [start_position, end_position] will be returned.

        feature_field: On which field would you like to retrieve the subset, 
                       either Feature.master_priority or Feature.client_priority
        client:        Required by client_priority to know on which client to list the priority.
        """

        if feature_field == Feature.client_priority:
            res = Feature.query.filter_by(
                   client_id=client.id
                ).filter(
                    feature_field >= start_position
                ).filter(
                    feature_field <= end_position
                )
        elif feature_field == Feature.master_priority:
            res = Feature.query.filter(
                    feature_field >= start_position
                ).filter(
                    feature_field <= end_position
                )
        else:
            print(feature_field)
            raise Exception('Invalid feature_field passed.')

        return res
