from marshmallow import Schema, fields


class FeatureSerializer(Schema):
    client_name = fields.Function(lambda obj: obj.client.name)
    created_by_name = fields.Function(lambda obj: "%s, %s" % (obj.created_by.last_name, obj.created_by.first_name))
    description = fields.Str()
    product_area_name = fields.Function(lambda obj: obj.product_area.name)

    class Meta:
        fields = (
            'id',
            'client_id',
            'client_name',
            'client_priority',
            'created_by_name',
            'date_created',
            'description',
            'product_area_id',
            'product_area_name',
            'target_date',
            'ticket_url',
            'title',
            )
