# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models

from snapshot_field import SnapshotModelField
from snapshot_field.utils import get_model_class

from .models import Example


def test_get_model_class():
    model_class = get_model_class('tests.Example')
    assert issubclass(model_class, models.Model)


def test_snapshot_field():
    field = SnapshotModelField(['tests.Example'])
    assert field.model_map
    field = SnapshotModelField(
        ['tests.Example', ['contenttypes.ContentType', {'fields': ['title']}]])
    assert field.model_map


def test_db_prep_value():
    field = SnapshotModelField([
        ['tests.Example', {'fields': ['name']}]
    ])
    client = Example.objects.create(name='test_name')
    db_value = field.get_db_prep_value(client, None)
    expect_data = [{"model": "tests.example", "pk": client.id,
                    "fields": {"name": client.name}}
                   ]
    assert json.loads(db_value) == expect_data
