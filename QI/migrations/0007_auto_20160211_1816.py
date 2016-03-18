# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0006_auto_20160205_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
            ],
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'Name of Place', blank=True)),
                ('place_id', models.ForeignKey(related_name='place_id', blank=True, to='QI.Place', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('img_url', models.CharField(max_length=200, verbose_name=b'Image URL', blank=True)),
                ('fulltext', models.TextField(verbose_name=b'Full Text', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('title', models.CharField(max_length=100, verbose_name=b'Title', blank=True)),
                ('date', models.CharField(max_length=20, verbose_name=b'Date', blank=True)),
                ('type_of_text', models.CharField(max_length=100, verbose_name=b'Type', blank=True)),
                ('call_no', models.CharField(max_length=100, verbose_name=b'call_no', blank=True)),
                ('person_id', models.ForeignKey(related_name='person_id_text', blank=True, to='QI.Person', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='text_id',
            field=models.ForeignKey(related_name='text_id', blank=True, to='QI.Text', null=True),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='org_id',
            field=models.ForeignKey(related_name='org_id', blank=True, to='QI.Org', null=True),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='person_id',
            field=models.ForeignKey(related_name='person_id', blank=True, to='QI.Person', null=True),
        ),
    ]
