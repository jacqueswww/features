from marshmallow import Schema


class ClientSerializer(Schema):

    class Meta:
        fields = (
            'id',
            'name',
            )
