# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20161201_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
