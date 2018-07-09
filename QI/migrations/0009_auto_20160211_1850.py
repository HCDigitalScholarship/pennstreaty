# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0008_auto_20160211_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('title', models.CharField(max_length=100, verbose_name=b'Title', blank=True)),
                ('date', models.CharField(max_length=20, verbose_name=b'Date', blank=True)),
                ('type_of_Manuscript', models.CharField(max_length=100, verbose_name=b'Type', blank=True)),
                ('call_no', models.CharField(max_length=100, verbose_name=b'call_no', blank=True)),
                ('person_id', models.ForeignKey(related_name='person_id_text', blank=True, to='QI.Person', null=True,on_delete=models.CASCADE)),
            ],
        ),
        migrations.RemoveField(
            model_name='text',
            name='person_id',
        ),
        migrations.RemoveField(
            model_name='page',
            name='text_id',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.AddField(
            model_name='page',
            name='Manuscript_id',
            field=models.ForeignKey(related_name='Manuscript_id', blank=True, to='QI.Manuscript', null=True,on_delete=models.CASCADE),
        ),
    ]
