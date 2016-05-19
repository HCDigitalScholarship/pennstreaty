# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0021_auto_20160519_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='org',
            old_name='name',
            new_name='organization_name',
        ),
    ]
