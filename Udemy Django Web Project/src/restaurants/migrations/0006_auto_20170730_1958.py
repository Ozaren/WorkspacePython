# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 23:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20170730_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaraunt',
            old_name='update',
            new_name='updated',
        ),
    ]