# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0014_auto_20171102_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tank',
            name='min_water',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
