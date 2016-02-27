from marshmallow import Schema, fields


class FeatureSerializer(Schema):
    client_name = fields.Function(lambda obj: obj.client.name)
    created_by_name = fields.Function(lambda obj: obj.created_by.name)
    description = fields.Str()
    product_area_name = fields.Function(lambda obj: obj.product_area.name)

    class Meta:
        fields = (
            'id',
            'client_id',
            'client_name',
            'created_by_name',
            'date_created',
            'product_area_id',
            'product_area_name',
            'target_date',
            'ticket_url',
            'title',
            )
