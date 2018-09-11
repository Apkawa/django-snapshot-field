from snapshot_field.utils import serialize_object, deserialize_object, serialize_object_json, deserialize_object_json
from tests.models import Example, ExampleReference


def test_simple_serialize_and_deserialization():
    obj = Example.objects.create(name='test_name')

    result = serialize_object(obj)
    obj_snapshot = deserialize_object(result)
    assert obj.id == obj_snapshot.id
    assert obj.name == obj_snapshot.name


def test_simple_serialize_and_deserialize_refs():
    obj = Example.objects.create(name='test_name')
    obj_ref = ExampleReference.objects.create(name='refname', ref=obj)

    result = serialize_object(obj_ref, refs=['ref'])
    obj_snapshot = deserialize_object(result)
    assert obj_ref.id == obj_snapshot.id
    assert obj_ref.name == obj_snapshot.name
    assert obj_ref.ref.name == obj.name


def test_json_serialize_deserialize():
    obj = Example.objects.create(name='test_name')
    obj_ref = ExampleReference.objects.create(name='refname', ref=obj)

    result = serialize_object_json(obj_ref, refs=['ref'])
    obj_snapshot = deserialize_object_json(result)
    assert obj_ref.id == obj_snapshot.id
    assert obj_ref.name == obj_snapshot.name
    assert obj_ref.ref.name == obj.name
