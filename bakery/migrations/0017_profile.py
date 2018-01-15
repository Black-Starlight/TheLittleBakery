# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 23:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bakery', '0016_auto_20180111_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('favs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_favorites', to='bakery.Recipes')),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_friends', to=settings.AUTH_USER_MODEL)),
                ('made', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_made', to='bakery.Recipes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]