from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Distance

from snapshot_field.fields import SnapshotModelField


class Example(models.Model):
    name = models.CharField(max_length=20)


class ExampleReference(models.Model):
    name = models.CharField(max_length=20)

    ref = models.ForeignKey(Example)


class MeasurementModel(models.Model):
    height = MeasurementField(measurement=Distance,
        blank=True,
        null=True)


class ExampleSnapshotModel(models.Model):
    snapshot = SnapshotModelField(null=True)
    snapshot_refs = SnapshotModelField(
        ['tests.Example', ['ExampleReference', {'refs': ['ref']}]], null=True
    )
