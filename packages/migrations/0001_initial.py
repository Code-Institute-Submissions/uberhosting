# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-21 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Package name', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('domains', models.IntegerField(default=1)),
                ('mail_space', models.IntegerField(default=0)),
                ('mail_address', models.IntegerField(default=0)),
                ('hosting_space', models.IntegerField(default=0)),
                ('hosting_databases', models.IntegerField(default=0)),
                ('apps', models.BooleanField(default=False)),
                ('highlight', models.BooleanField(default=False)),
                ('sftp', models.IntegerField(default=0)),
            ],
        ),
    ]
