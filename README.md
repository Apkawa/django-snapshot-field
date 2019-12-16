[![PyPi](https://img.shields.io/pypi/v/django-snapshot-field.svg)](https://pypi.python.org/pypi/django-snapshot-field)
[![Build Status](https://travis-ci.org/Apkawa/django-snapshot-field.svg?branch=master)](https://travis-ci.org/Apkawa/django-snapshot-field)
[![Codecov](https://codecov.io/gh/Apkawa/django-snapshot-field/branch/master/graph/badge.svg)](https://codecov.io/gh/Apkawa/django-snapshot-field)
[![Requirements Status](https://requires.io/github/Apkawa/django-snapshot-field/requirements.svg?branch=master)](https://requires.io/github/Apkawa/django-snapshot-field/requirements/?branch=master)
[![PyUP](https://pyup.io/repos/github/Apkawa/django-snapshot-field/shield.svg)](https://pyup.io/repos/github/Apkawa/django-snapshot-field)
[![PyPI](https://img.shields.io/pypi/pyversions/django-snapshot-field.svg)](https://pypi.python.org/pypi/django-snapshot-field)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Project for merging different file types, as example easy thumbnail image and unpacking archive in one field

# Installation

```bash
    pip install django-snapshot-field
```

or from git

```bash
pip install -e git+https://githib.com/Apkawa/django-snapshot-field.git#egg=django-snapshot-field
```

## Django and python version

* python-2.7 - django>=1.8,<=1.11
* python-3.4 - django>=1.8,<=1.11
* python-3.5 - django>=1.8,<=1.11
* python-3.6 - django>=1.11


# Usage

```python
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
        ['tests.Example', ['ExampleReference', {'fields': ['name', 'ref'], 'refs': ['ref']}]]
    )
```

# Contributing

## run example app

```bash
pip install -r requirements.txt
./test/manage.py migrate
./test/manage.py runserver
```

## run tests

by pip and venv
```bash
pip install -r requirements.txt
pytest
tox
```

or pipenv

```bash
pipenv install -r requirements.txt
pipenv run - pytest
pipenv run - tox

```

## publish pypi

```bash
python setup.py publish
```






