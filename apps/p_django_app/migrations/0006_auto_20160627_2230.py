# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_django_app', '0005_auto_20160627_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='name',
            new_name='user_id',
        ),
    ]