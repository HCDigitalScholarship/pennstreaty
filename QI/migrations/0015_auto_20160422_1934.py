# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0014_organization_place_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='uri_lcnaf',
            new_name='lcnaf_uri',
        ),
        migrations.AddField(
            model_name='place',
            name='date',
            field=models.CharField(max_length=20, verbose_name=b'Date', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_type',
            field=models.CharField(default=b'placeName', max_length=2, verbose_name=b'Place Type', blank=True, choices=[(b'placeName', b'Place Name'), (b'geogName', b'Geography Name')]),
        ),
    ]
