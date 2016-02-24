from features_app.utils import set_fields_from_dict
from features.models.feature import Feature

class FeatureServices:

    @staticmethod
    def create(params, action_by, commit=True):
        feature = Feature()

        set_fields_from_dict(feature, params, Feature._fields)

        feature.created_by = action_by

        if commit:
            feature.save()

        return feature
