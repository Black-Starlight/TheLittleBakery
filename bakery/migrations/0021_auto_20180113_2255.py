# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0020_auto_20180113_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.CharField(max_length=17),
        ),
    ]
