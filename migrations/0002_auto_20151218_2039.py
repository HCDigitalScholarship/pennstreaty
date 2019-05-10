# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='review_status',
            field=models.CharField(max_length=50, verbose_name=b'TEI ID'),
        ),
    ]
