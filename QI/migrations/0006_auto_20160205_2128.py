# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0005_auto_20160205_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='id_tei',
            field=models.CharField(default=0, max_length=50, verbose_name=b'TEI ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationshiptype',
            name='id_tei',
            field=models.CharField(default=0, max_length=50, verbose_name=b'TEI ID'),
            preserve_default=False,
        ),
    ]
