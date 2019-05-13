# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0020_auto_20160519_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='place_id',
            field=models.ForeignKey(related_name='place_id', blank=True, to='QI.Place', null=True, on_delete=models.CASCADE),
        ),
    ]
