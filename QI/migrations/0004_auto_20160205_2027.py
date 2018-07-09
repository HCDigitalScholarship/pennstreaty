# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0003_place_county'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.ForeignKey(related_name='objectid', blank=True, to='QI.Person', null=True,on_delete=models.CASCADE,)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationship_type', models.CharField(max_length=100, verbose_name=b'Relationship Type', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name of Place', blank=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_type_id',
            field=models.ForeignKey(related_name='relationshipType', blank=True, to='QI.RelationshipType', null=True,on_delete=models.CASCADE,),
        ),
        migrations.AddField(
            model_name='relationship',
            name='subject_id',
            field=models.ForeignKey(related_name='subjectid', blank=True, to='QI.Person', null=True,on_delete=models.CASCADE,),
        ),
    ]
