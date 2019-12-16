# -*- coding: utf-8 -*-
import six

if not six.PY2:
    try:
        from django_measurement.models import MeasurementField
        MeasurementField.value_to_string = lambda self, obj: (
            self.get_prep_value(self.value_from_object(obj))
        )
    except ImportError:
        pass
