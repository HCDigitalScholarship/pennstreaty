# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0022_auto_20160519_1450'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
