from marshmallow import Schema, fields


class ClientSerializer(Schema):

    class Meta:
        fields = (
            'id',
            'name',
            )
