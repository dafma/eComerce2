# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 20:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='SignUp',
        ),
    ]
