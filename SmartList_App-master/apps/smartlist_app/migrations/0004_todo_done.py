# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlist_app', '0003_auto_20170823_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]