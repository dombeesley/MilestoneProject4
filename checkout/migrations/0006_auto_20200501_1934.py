# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-01 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200501_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]