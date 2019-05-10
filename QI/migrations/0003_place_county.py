# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0002_auto_20151218_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='county',
            field=models.CharField(max_length=100, verbose_name=b'County', blank=True),
        ),
    ]
