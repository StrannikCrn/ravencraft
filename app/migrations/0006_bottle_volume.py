# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-24 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180424_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='volume',
            field=models.CharField(default='', max_length=20, verbose_name='Объем'),
        ),
    ]