from marshmallow import Schema


class FeatureSerializer(Schema):

    class Meta:
        fields = (
            'id',
            'title',
            'description'
            )
