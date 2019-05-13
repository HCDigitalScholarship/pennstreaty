# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0017_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_type',
            field=models.CharField(default=b'placeName', max_length=30, verbose_name=b'Place Type', blank=True, choices=[(b'placeName', b'Place Name'), (b'geogName', b'Geography Name')]),
        ),
    ]
