# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0011_auto_20160219_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='categories', null=True, to='QI.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='affiliations',
            field=models.ManyToManyField(to='QI.Org', blank=True),
        ),
    ]
