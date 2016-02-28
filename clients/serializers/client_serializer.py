from features.queries.feature_queries import FeatureQueries
from marshmallow import Schema, fields


class ClientSerializer(Schema):
    max_client_priority = fields.Method("get_max_client_priority")

    class Meta:
        fields = (
            'id',
            'name',
            'max_client_priority'
            )

    def get_max_client_priority(self, obj):
        res = FeatureQueries.get_max_client_priority_client(obj)

        return res
