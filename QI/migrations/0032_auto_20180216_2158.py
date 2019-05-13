# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0031_manuscript_transcribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuscript',
            name='transcribed',
            field=models.BooleanField(default=True, verbose_name=b'Transcribed'),
        ),
    ]
