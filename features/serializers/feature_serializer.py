from marshmallow import Schema, fields


class SongSerializer(Schema):
    id = fields.Str()

    class Meta:
        fields = (
            'id',
            'title',
            'description'
            )
