from datetime import datetime

from features_app.utils import set_fields_from_dict, get_fields
from features_app.db import db
from features.models.feature import Feature
from features.queries.feature_queries import FeatureQueries
from users.models.user import User


class FeatureServices:

    @staticmethod
    def create(params, action_by, commit=True):
        assert isinstance(params, dict)

        feature = Feature()

        model_fields = get_fields(Feature)
        set_fields_from_dict(feature, params, model_fields)

        feature.created_by = action_by

        db.session.add(feature)
        if commit:
            db.session.commit()

        return feature

    @staticmethod
    def update(feature, params, action_by, commit=True):
        assert isinstance(feature, Feature)
        assert isinstance(params, dict)

        model_fields = get_fields(Feature)
        set_fields_from_dict(feature, params, model_fields)

        feature.modified_by_id = action_by.id
        feature.date_modified = datetime.now()

        if commit:
            db.session.commit()

        return feature

    @classmethod
    def reorder_client_priority(cls, client, action_by):
        """
        Reapply client priority numbering if the sequence has a gap 
        (used if you delete a feature).
        """
        features = FeatureQueries.get_all_by_client(client, order_by_client_priority=True)

        i = 1
        for feature in features:
            cls.update(feature, {'client_priority': i}, commit=False, action_by=action_by)
            i += 1

        db.session.commit()

    @classmethod
    def delete(cls, feature, action_by, commit=True):
        """
        Delete a feature ticket.
        """
        # TODO: see if we need make this a soft delete ?
        assert isinstance(feature, Feature)
        
        client = feature.client
        db.session.delete(feature)

        if commit:
            db.session.commit()
            cls.reorder_client_priority(client, action_by)

        return True
