from datetime import datetime

from features_app.utils import set_fields_from_dict, get_fields
from features_app.db import db
from features.models.feature import Feature
from users.models.user import User


class FeatureServices:

    @staticmethod
    def create(params, action_by, commit=True):
        assert isinstance(action_by, User)
        assert isinstance(params, dict)

        feature = Feature()

        model_fields = get_fields(Feature)
        set_fields_from_dict(feature, params, model_fields)

        feature.created_by = action_by

        if commit:
            db.session.add(feature)
            db.session.commit()

        return feature

    @staticmethod
    def update(feature, params, action_by, commit=True):
        assert isinstance(feature, Feature)
        assert isinstance(action_by, User)
        assert isinstance(params, dict)

        model_fields = get_fields(Feature)
        set_fields_from_dict(feature, params, model_fields)

        if commit:
            feature.modified_by_id = action_by.id
            feature.date_modified = datetime.datetime.now()

        return feature
