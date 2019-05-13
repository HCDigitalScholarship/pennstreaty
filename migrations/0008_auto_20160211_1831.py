# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0007_auto_20160211_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='affiliations',
            field=models.ManyToManyField(to='QI.Org'),
        ),
        migrations.AlterField(
            model_name='org',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name of Organization', blank=True),
        ),
    ]
