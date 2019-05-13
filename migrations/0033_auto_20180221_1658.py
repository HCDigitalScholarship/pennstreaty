# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0032_auto_20180216_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingTranscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transcription', models.TextField()),
                ('author', models.CharField(max_length=50, blank=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='transcribed',
            field=models.BooleanField(default=True, verbose_name=b'Transcribed'),
        ),
        migrations.AddField(
            model_name='pendingtranscription',
            name='doc',
            field=models.ForeignKey(to='QI.Page', on_delete=models.CASCADE),
        ),
    ]
