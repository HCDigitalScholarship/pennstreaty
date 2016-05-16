# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0011_auto_20160219_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='affiliations',
            field=models.ManyToManyField(to='QI.Org', blank=True),
        ),
    ]
