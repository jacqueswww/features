from features.queries.feature_queries import FeatureQueries
from marshmallow import Schema


class ClientSerializer(Schema):
    max_client_priority = fields. fields.Method("get_max_client_priority")

    class Meta:
        fields = (
            'id',
            'name',
            'max_client_priority'
            )

    def get_max_client_priority(self, obj):
        return FeatureQueries.get_max_client_priority(obj)
