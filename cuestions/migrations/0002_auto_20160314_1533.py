# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='cuestions.Answer'),
        ),
    ]
