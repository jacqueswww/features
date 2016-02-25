from marshmallow import Schema


class ProductAreaSerializer(Schema):

    class Meta:
        fields = (
            'id',
            'name'
        )

