from snapshot_field.utils import serialize_object
from tests.models import Example


def test_db_prep_value():
    obj = Example.objects.create(name='test_name')

    result = serialize_object(obj)
    return serialize_object(result)
