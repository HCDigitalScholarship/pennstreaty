# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('organization_name', models.CharField(max_length=100, verbose_name=b'Name of Organization', blank=True)),
                ('notes', models.TextField(verbose_name=b'Note Field', blank=True)),
                ('associated_spellings', models.TextField(verbose_name=b'Associated Spellings/Names', blank=True)),
                ('PYM_index', models.TextField(verbose_name=b'PYM Index', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_status', models.BooleanField(default=1)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('uri_lcnaf', models.CharField(max_length=50, verbose_name=b'URI LCNAF', blank=True)),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Last Name', blank=True)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First Name', blank=True)),
                ('middle_name', models.CharField(max_length=100, verbose_name=b'Middle Name', blank=True)),
                ('display_name', models.CharField(max_length=100, verbose_name=b'Display Name', blank=True)),
                ('other_names', models.TextField(verbose_name=b'Other Names', blank=True)),
                ('birth_date', models.CharField(max_length=20, verbose_name=b'Birth Date', blank=True)),
                ('death_date', models.CharField(max_length=20, verbose_name=b'Death Date', blank=True)),
                ('gender', models.CharField(max_length=20, verbose_name=b'Gender', blank=True)),
                ('affiliation1', models.CharField(max_length=45, verbose_name=b'Affiliation 1', blank=True)),
                ('affiliation2', models.CharField(max_length=45, verbose_name=b'Affiliation 2', blank=True)),
                ('notes', models.TextField(verbose_name=b'Note Field', blank=True)),
                ('bio_notes', models.TextField(verbose_name=b'Biography Note Field', blank=True)),
                ('data_notes', models.TextField(verbose_name=b'Data Note Field', blank=True)),
                ('citations', models.TextField(verbose_name=b'Citations', blank=True)),
                ('PYM_index', models.TextField(verbose_name=b'PYM Index', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tei', models.CharField(max_length=50, verbose_name=b'TEI ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Name of Place', blank=True)),
                ('state', models.CharField(max_length=20, verbose_name=b'State', blank=True)),
                ('latitude', models.CharField(max_length=15, null=True, verbose_name=b'Latitude', blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, verbose_name=b'Longitude', blank=True)),
                ('notes', models.TextField(verbose_name=b'Description Field', blank=True)),
                ('notes2', models.TextField(verbose_name=b'Description Field', blank=True)),
                ('place_type', models.CharField(default=b'PN', max_length=2, verbose_name=b'Place Type', blank=True, choices=[(b'PN', b'Place Name'), (b'GN', b'Geography Name')])),
                ('alternate', models.TextField(verbose_name=b'Alternate Names', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=50, verbose_name=b'Role_Type', blank=True)),
                ('description', models.TextField(verbose_name=b'Description of Role', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Role Types',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='birth_place',
            field=models.ForeignKey(related_name='birthplace', blank=True, to='QI.Place', null=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='person',
            name='death_place',
            field=models.ForeignKey(related_name='deathplace', blank=True, to='QI.Place', null=True,on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(related_name='person_Role_1', blank=True, to='QI.RoleType', null=True,on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='person',
            name='role2',
            field=models.ForeignKey(related_name='person_Role_2', blank=True, to='QI.RoleType', null=True,on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='person',
            name='role3',
            field=models.ForeignKey(related_name='person_Role_3', blank=True, to='QI.RoleType', null=True,on_delete=models.CASCADE),
        ),
    ]
