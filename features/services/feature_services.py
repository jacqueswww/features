from datetime import datetime

from features_app.utils import set_fields_from_dict, get_fields
from features_app.db import db
from features.models.feature import Feature
from features.queries.feature_queries import FeatureQueries
from clients.queries.client_queries import ClientQueries


class FeatureServices:

    @classmethod
    def create(cls, params, action_by, commit=True):
        assert isinstance(params, dict)

        feature = Feature()

        exclusion_list = ['modified_by_id'] + cls.exclude_master_priority_param(params, action_by)  # may master priority be set?
        model_fields = get_fields(Feature)

        # apply all fields to object.
        set_fields_from_dict(feature, params, model_fields, exclude_fields=exclusion_list)

        cls.sanitise_target_date(feature, params)
        cls.apply_priority_shifts(feature, params, action_by)

        feature.created_by = action_by

        db.session.add(feature)
        if commit:
            db.session.commit()

        return feature


    @classmethod
    def update(cls, feature, params, action_by, commit=True):
        assert isinstance(feature, Feature)
        assert isinstance(params, dict)

        # old_client_priority = feature.client_priority
        # new_client_priority = params.get('client_priority', feature.client_priority)

        model_fields = get_fields(Feature)
        exclusion_list = ["date_created", "date_modified", "created_by_id"]
        exclusion_list += cls.exclude_master_priority_param(params, action_by)   # may master priority be set?

        cls.apply_priority_shifts(feature, params, action_by, is_update=True)

        # apply all fields to object.
        set_fields_from_dict(feature, params, model_fields, exclude_fields=exclusion_list)

        cls.sanitise_target_date(feature, params)
        
        feature.modified_by_id = action_by.id
        feature.date_modified = datetime.now()

        if commit:
            db.session.commit()

        return feature

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
            cls.reorder_priorities(client)

        return True

    @staticmethod
    def exclude_master_priority_param(params, action_by):
        """ Whether to exclude master priority from list """

        if all([action_by.is_super, "master_priority" in params]):
            return []
        else:
            return ["master_priority"]
         
    @classmethod
    def apply_priority_shifts(cls, feature, params, action_by, is_update=False):
        # shift the client priority up so we can save into the proper position.

        client = ClientQueries.get_by_id(params.get('client_id', feature.client_id))
        max_client_priority = FeatureQueries.get_max_client_priority_client(client)
        max_master_priority = FeatureQueries.get_max_master_priority()
       
        run_client_shift = True
        run_master_shift = True

        if is_update:  # handle subset if it is an update.
            old_client_priority = feature.client_priority
            old_master_priority = feature.master_priority

        else:
            old_client_priority = max_client_priority
            old_master_priority = max_master_priority

        new_master_priority = params.get('master_priority', 1)
        new_client_priority = params.get('client_priority', 1)

        if is_update:
            if new_client_priority == old_client_priority:
                run_client_shift = False
            if new_master_priority == old_master_priority:
                run_master_shift = False

        if run_client_shift:
            cls.shift_priority(
                old_priority=old_client_priority,
                new_priority=new_client_priority,
                max_priority=max_client_priority,
                feature_field=Feature.client_priority,
                client=client
                )

        if run_master_shift:
            # shift master priority (if allowed).
            if all([action_by.is_super, "master_priority" in params]):  # may master priority be set, shift priorities accordingly.
                cls.shift_priority(
                    old_priority=old_master_priority,
                    new_priority=new_master_priority,
                    max_priority=max_master_priority,
                    feature_field=Feature.master_priority
                    )
            else:  # otherwise we just add it to the end of the list.
                feature.master_priority = max_master_priority + 1

    @staticmethod
    def sanitise_target_date(feature, params):
        target_date = params.get('target_date')
        if target_date:
            if'T' in target_date:
                feature.target_date = datetime.strptime(target_date.split('T')[0], '%Y-%m-%d').date()
            else:
                feature.target_date = datetime.strptime(target_date, '%Y-%m-%d').date()

    @classmethod
    def shift_priority(cls, old_priority, new_priority, max_priority, feature_field, client=None):
        """
        Given a position in priority list, shift up other features so there is a position free.
        Can either shift list up or down.

        feature_field: On which field shift the list, 
                       either Feature.master_priority or Feature.client_priority
        action
        client:        Client is only required for Feature.client_priority
        """

        # if our client priority is at the end, don't shift anything.
        if new_priority > max_priority:
            return None

        if new_priority <= old_priority:
            # print('shifting down')
            features = FeatureQueries.get_by_priority_subset(
                    client=client,
                    start_position=new_priority,
                    end_position=old_priority,
                    feature_field=feature_field
                )
            features.update({
                feature_field: feature_field + 1  # shift it down.
                })
        elif new_priority >= old_priority:
            # print('shifting up')
            features = FeatureQueries.get_by_priority_subset(
                    client=client,
                    start_position=old_priority,
                    end_position=new_priority,
                    feature_field=feature_field
                )
            features.update({
                feature_field: feature_field - 1 # shift it up.
                })

        db.session.commit()
        return None

    @classmethod
    def reorder_priorities(cls, client):
        """
        Reapply priority numbering if the sequence has a gap 
        (used if you delete a feature).
        """

        features = FeatureQueries.get_all_by_client(client, order_by_client_priority=True)

        i = 1
        for feature in features:
            feature.client_priority = i
            i += 1

        db.session.commit()

        features = FeatureQueries.get_all_ordered_by_master_priority()

        i = 1
        for feature in features:
            feature.master_priority = i
            i += 1

        db.session.commit()
