from sqlalchemy.orm import class_mapper
import sqlalchemy


def get_fields(aModel):
    """ Return the fields on a sql alchemy model. """
    field_list = []
    for prop in class_mapper(aModel).iterate_properties:
        if isinstance(prop, sqlalchemy.orm.ColumnProperty):
            field_list.append(prop.key)

    return field_list


def set_fields_from_dict(obj, _dict, fields, exclude_fields=[]):
    final_fields = _dict.keys() - exclude_fields
    for field_name in final_fields:
        if field_name in _dict:
            value = _dict.get(field_name)
            if isinstance(value, str):
                value = value.strip()
            setattr(obj, field_name, value)
