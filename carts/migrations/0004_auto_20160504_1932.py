# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_productfeatured_text_css_color'),
        ('carts', '0003_remove_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='carts.CartItem', to='products.Variation'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
    ]
