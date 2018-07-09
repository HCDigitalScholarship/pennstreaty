# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0030_auto_20161222_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscript',
            name='transcribed',
            field=models.BooleanField(default=True),
        ),
    ]
