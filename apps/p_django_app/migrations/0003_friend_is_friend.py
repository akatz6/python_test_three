# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_django_app', '0002_auto_20160627_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='is_friend',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
