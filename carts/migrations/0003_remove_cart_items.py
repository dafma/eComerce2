# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20160504_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
    ]
