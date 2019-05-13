# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QI', '0029_place_place_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscript',
            name='location',
            field=models.CharField(max_length=20, verbose_name=b'Location', blank=True),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='org_id',
            field=models.ForeignKey(related_name='org_id_text', blank=True, to='QI.Org', null=True,on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='org_name',
            field=models.CharField(max_length=200, verbose_name=b'Organization', blank=True),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='person_name',
            field=models.CharField(max_length=100, verbose_name=b'Author', blank=True),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='summary',
            field=models.CharField(max_length=1000, verbose_name=b'summary', blank=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='date',
            field=models.CharField(max_length=50, verbose_name=b'Date', blank=True),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='id_tei',
            field=models.CharField(max_length=100, verbose_name=b'TEI ID'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='title',
            field=models.CharField(max_length=300, verbose_name=b'Title', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='PYM_index',
            field=models.TextField(max_length=500, verbose_name=b'PYM Index', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='associated_spellings',
            field=models.TextField(max_length=500, verbose_name=b'Associated Spellings/Names', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='bio_notes',
            field=models.TextField(max_length=500, verbose_name=b'Description Field', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='citations',
            field=models.TextField(max_length=500, verbose_name=b'Description Field', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='data_notes',
            field=models.CharField(max_length=500, verbose_name=b'LCNAF URI', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='date_dissolved',
            field=models.CharField(max_length=500, verbose_name=b'Date Founded', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='date_founded',
            field=models.CharField(max_length=500, verbose_name=b'Date Founded', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='id_tei',
            field=models.CharField(max_length=500, verbose_name=b'TEI ID'),
        ),
        migrations.AlterField(
            model_name='org',
            name='lcnaf_uri',
            field=models.CharField(max_length=500, verbose_name=b'LCNAF URI', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='notes',
            field=models.CharField(max_length=500, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='organization_name',
            field=models.CharField(max_length=500, verbose_name=b'Name of Organization', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='other_names',
            field=models.CharField(max_length=500, verbose_name=b'Other Names of Organization', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='PYM_index',
            field=models.TextField(max_length=100, verbose_name=b'PYM Index', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio_notes',
            field=models.TextField(max_length=100, verbose_name=b'Biography Note Field', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.CharField(max_length=100, verbose_name=b'Birth Date', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='citations',
            field=models.TextField(max_length=100, verbose_name=b'Citations', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='data_notes',
            field=models.TextField(max_length=100, verbose_name=b'Data Note Field', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_date',
            field=models.CharField(max_length=100, verbose_name=b'Death Date', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='id_tei',
            field=models.CharField(max_length=100, verbose_name=b'TEI ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lcnaf_uri',
            field=models.CharField(max_length=100, verbose_name=b'URI LCNAF', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(max_length=100, verbose_name=b'Note Field', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='other_names',
            field=models.TextField(max_length=100, verbose_name=b'Other Names', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='review_status',
            field=models.CharField(max_length=100, verbose_name=b'TEI ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='alternate',
            field=models.TextField(max_length=200, verbose_name=b'Alternate Names', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='date',
            field=models.CharField(max_length=100, verbose_name=b'Date', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='id_tei',
            field=models.CharField(max_length=100, verbose_name=b'TEI ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='notes',
            field=models.TextField(max_length=500, verbose_name=b'Description Field', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='notes2',
            field=models.TextField(max_length=500, verbose_name=b'Description Field', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='state',
            field=models.CharField(max_length=100, verbose_name=b'State', blank=True),
        ),
    ]
