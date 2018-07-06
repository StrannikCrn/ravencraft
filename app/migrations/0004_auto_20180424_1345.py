# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-24 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180424_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='ABV',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='ABV'),
        ),
        migrations.AlterField(
            model_name='bottle',
            name='image_index_dark',
            field=models.ImageField(null=True, upload_to='app/static/images/bottles', verbose_name='Картинка на главную (затемнённая)'),
        ),
    ]
