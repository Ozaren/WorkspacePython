# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaraunt_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaraunt',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
