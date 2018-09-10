from django.db import models


class Example(models.Model):
    name = models.CharField(max_length=20)


class ExampleReference(models.Model):
    name = models.CharField(max_length=20)

    ref = models.ForeignKey(Example)



