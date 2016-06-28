# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='poking',
            name='who_poked',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='register',
            name='last_name',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Poking',
        ),
    ]
