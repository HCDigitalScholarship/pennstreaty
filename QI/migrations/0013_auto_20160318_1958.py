# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0012_auto_20160318_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='QI.Category', blank=True),
        ),
    ]
