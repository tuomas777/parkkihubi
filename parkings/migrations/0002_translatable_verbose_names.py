# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='operator',
            options={'verbose_name': 'operator', 'verbose_name_plural': 'operators'},
        ),
        migrations.AlterModelOptions(
            name='parking',
            options={'verbose_name': 'parking', 'verbose_name_plural': 'parkings'},
        ),
    ]