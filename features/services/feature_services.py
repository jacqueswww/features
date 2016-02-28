from datetime import datetime

from features_app.utils import set_fields_from_dict, get_fields
from features_app.db import db
from features.models.feature import Feature
from features.queries.feature_queries import FeatureQueries
from clients.queries.client_queries import ClientQueries
from users.models.user import User


class FeatureServices:

    @classmethod
    def create(cls, params, action_by, commit=True):
        assert isinstance(params, dict)

        feature = Feature()

        # shift the client priority up so we can save into the proper position.
        client = ClientQueries.get_by_id(params.get('client_id'))
        max_client_priority = FeatureQueries.get_max_client_priority_client(client)
        cls.shift_client_priority(client, max_client_priority, params.get('client_priority', 1), action_by)

        model_fields = get_fields(Feature)
        set_fields_from_dict(feature, params, model_fields)

        target_date = params.get('target_date')
        if target_date:
            feature.target_date = datetime.strptime(target_date.split('T')[0], '%Y-%m-%d').date()
        else:
            feature.target_date = datetime.now().date()

        feature.created_by = action_by

        db.session.add(feature)
        if commit:
            db.session.commit()

        return feature

    @classmethod
    def shift_client_priority(cls, client, old_client_priority, new_client_priority, action_by):
        """
        Given a position in client_priority list, shift up other features so there is a position free.
        Can either shift list up or down.
        """
        max_client_priority = FeatureQueries.get_max_client_priority_client(client)

        # if our client priority is at the end
        if new_client_priority > max_client_priority:
            return None

        if new_client_priority < old_client_priority:
            # get all features from position, then increment their priorities.
            features = FeatureQueries.get_by_client_priority_subset(
                    client=client,
                    start_position=new_client_priority,
                    end_postion=old_client_priority
                )
            features.update({
                Feature.client_priority: Feature.client_priority + 1  # shift it down.
                })
        elif new_client_priority > old_client_priority:
            features = FeatureQueries.get_by_client_priority_subset(
                    client=client,
                    start_position=old_client_priority,
                    end_postion=new_client_priority
                )
            features.update({
                Feature.client_priority: Feature.client_priority - 1 # shift it up.
                })


        db.session.commit()
        return None

    @classmethod
    def update(cls, feature, params, action_by, commit=True):
        assert isinstance(feature, Feature)
        assert isinstance(params, dict)

        old_client_priority = feature.client_priority
        new_client_priority = params.get('client_priority', feature.client_priority)

        if old_client_priority != new_client_priority:
            cls.shift_client_priority(feature.client, old_client_priority, params.get('client_priority', 1), action_by)

        model_fields = get_fields(Feature)
        set_fields_from_dict(feature, params, model_fields)

        feature.modified_by_id = action_by.id
        feature.date_modified = datetime.now()

        if commit:
            db.session.commit()

        return feature

    @classmethod
    def reorder_client_priority_gap(cls, client, action_by):
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
            cls.reorder_client_priority_gap(client, action_by)

        return True
