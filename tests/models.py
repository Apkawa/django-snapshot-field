from django.db import models

from snapshot_field.fields import SnapshotModelField


class Example(models.Model):
    name = models.CharField(max_length=20)


class ExampleReference(models.Model):
    name = models.CharField(max_length=20)

    ref = models.ForeignKey(Example)


class ExampleSnapshotModel(models.Model):
    snapshot = SnapshotModelField(null=True)
    snapshot_refs = SnapshotModelField(
        ['tests.Example', ['ExampleReference', {'refs': ['ref']}]]
    )
