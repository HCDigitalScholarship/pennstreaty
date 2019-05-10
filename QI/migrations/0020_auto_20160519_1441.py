# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0019_auto_20160519_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='PYM_index',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='associated_spellings',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bio_notes',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='citations',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='data_notes',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='date_dissolved',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='date_founded',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='lcnaf_uri',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='org_type',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='other_names',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='place_id',
        ),
        migrations.AddField(
            model_name='org',
            name='PYM_index',
            field=models.TextField(verbose_name=b'PYM Index', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='associated_spellings',
            field=models.TextField(verbose_name=b'Associated Spellings/Names', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='bio_notes',
            field=models.TextField(verbose_name=b'Description Field', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='citations',
            field=models.TextField(verbose_name=b'Description Field', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='data_notes',
            field=models.CharField(max_length=50, verbose_name=b'LCNAF URI', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='date_dissolved',
            field=models.CharField(max_length=20, verbose_name=b'Date Founded', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='date_founded',
            field=models.CharField(max_length=20, verbose_name=b'Date Founded', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='lcnaf_uri',
            field=models.CharField(max_length=50, verbose_name=b'LCNAF URI', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='notes',
            field=models.CharField(max_length=50, verbose_name=b'Notes', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='org_type',
            field=models.CharField(max_length=70, verbose_name=b'Oraganization Type', blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='other_names',
            field=models.CharField(max_length=200, verbose_name=b'Other Names of Organization', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='place_id',
            field=models.ForeignKey(related_name='place_id2', blank=True, to='QI.Place', null=True,on_delete=models.CASCADE),
        ),
    ]
