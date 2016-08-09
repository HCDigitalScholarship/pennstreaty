# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0004_auto_20160205_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'Name of Place', blank=True)),
                ('latitude', models.CharField(max_length=15, null=True, verbose_name=b'Latitude', blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, verbose_name=b'Longitude', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('loc_type', models.CharField(max_length=200, verbose_name=b'Name of Place', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='loc_type_id',
            field=models.ForeignKey(related_name='LocationType', blank=True, to='QI.LocType', null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='location_id',
            field=models.ForeignKey(related_name='Location', blank=True, to='QI.Location', null=True),
        ),
    ]
