# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-26 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200126_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Robin Kaal', max_length=200),
            preserve_default=False,
        ),
    ]
