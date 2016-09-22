# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0024_auto_20160909_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='uri_lcnaf',
            new_name='lcnaf_uri',
        ),
    ]
