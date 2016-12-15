# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 03:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0002_social'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'Social media links'},
        ),
        migrations.AddField(
            model_name='thing',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
