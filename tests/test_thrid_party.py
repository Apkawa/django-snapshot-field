# -*- coding: utf-8 -*-
from measurement.measures import Distance

from snapshot_field.utils import serialize_object_json, deserialize_object_json
from tests.models import MeasurementModel, ExampleSnapshotModel


def test_measurement_json_serialize_deserialize():
    obj = MeasurementModel.objects.create(height=Distance(cm=20.0))

    result = serialize_object_json(obj)
    obj_snapshot = deserialize_object_json(result)
    assert obj_snapshot
    assert obj_snapshot.height == obj.height


def test_model_save():
    obj = MeasurementModel.objects.create(height=Distance(cm=12.5))

    snap = ExampleSnapshotModel.objects.create(snapshot=obj)
    assert snap.snapshot
    assert snap.snapshot.height == obj.height
    snap = ExampleSnapshotModel.objects.get()
    assert snap.snapshot
    assert snap.snapshot.height == obj.height
