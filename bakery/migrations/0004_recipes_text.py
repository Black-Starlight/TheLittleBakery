# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0003_auto_20171221_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='text',
            field=models.TextField(default='', max_length=200),
        ),
    ]
