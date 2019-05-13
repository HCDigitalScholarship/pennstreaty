# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0013_auto_20160318_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='place_id',
            field=models.ForeignKey(related_name='place_id2', blank=True, to='QI.Place', null=True,on_delete=models.CASCADE),
        ),
    ]
