# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-13 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180513_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.BeerGroup', verbose_name='Тип пива'),
        ),
    ]
