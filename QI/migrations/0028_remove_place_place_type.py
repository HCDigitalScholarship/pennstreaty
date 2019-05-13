# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0027_auto_20160909_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_type',
        ),
    ]
