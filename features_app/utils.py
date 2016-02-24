
def set_fields_from_dict(obj, _dict, fields, exclude_fields=[]):
    final_fields = _dict.keys() - exclude_fields
    for field_name in final_fields:
        if field_name in _dict:
            value = _dict.get(field_name)
            if isinstance(value, str):
                value = value.strip()
            setattr(obj, field_name, value)
