# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_django_app', '0006_auto_20160627_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friends_with',
        ),
    ]