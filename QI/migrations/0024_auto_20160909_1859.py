# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0023_delete_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='lcnaf_uri',
            new_name='uri_lcnaf',
        ),
    ]
