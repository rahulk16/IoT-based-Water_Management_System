# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0008_plant_data_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_data',
            name='raining',
            field=models.BooleanField(default=True),
        ),
    ]