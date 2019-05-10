# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0015_auto_20160422_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='bio_notes',
            field=models.TextField(verbose_name=b'Description Field', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='citations',
            field=models.TextField(verbose_name=b'Description Field', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='data_notes',
            field=models.CharField(max_length=50, verbose_name=b'LCNAF URI', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='date_dissolved',
            field=models.CharField(max_length=20, verbose_name=b'Date Founded', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='date_founded',
            field=models.CharField(max_length=20, verbose_name=b'Date Founded', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='lcnaf_uri',
            field=models.CharField(max_length=50, verbose_name=b'LCNAF URI', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='org_type',
            field=models.CharField(max_length=70, verbose_name=b'Oraganization Type', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='other_names',
            field=models.CharField(max_length=200, verbose_name=b'Other Names of Organization', blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='notes',
            field=models.CharField(max_length=50, verbose_name=b'Notes', blank=True),
        ),
    ]
