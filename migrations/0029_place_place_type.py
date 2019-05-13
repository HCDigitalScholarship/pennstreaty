# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0028_remove_place_place_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.CharField(default=b'placeName', max_length=30, verbose_name=b'Place Type', blank=True, choices=[(b'placeName', b'Place Name'), (b'geogName', b'Geography Name')]),
        ),
    ]
