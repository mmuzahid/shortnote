# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='rolename',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]