from django.core import serializers
from django.db import models


def serialize_object(obj, depth=0, fields=None):
    ser_obj = serializers.serialize('python', [obj], fields=fields)[0]

    fk_fields = {f.name for f in obj._meta.fields if
                 isinstance(f, (models.ForeignKey, models.OneToOneField))}
    if depth <= 0:
        return ser_obj
    refs = {}
    for f in fk_fields:
        if not fields or f in fields:
            n_obj = getattr(ser_obj, f)
            sub_fields = None  # TODO
            if n_obj:
                refs[f] = serialize_object(obj, depth - 1, sub_fields)

    ser_obj['refs'] = refs
    return ser_obj


def serialize_object_json():
    pass
