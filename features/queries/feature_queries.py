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
