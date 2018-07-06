# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-12 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180511_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsBottleSpecid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bottle', to='app.Bottle', verbose_name='Бутылка')),
                ('news_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_item', to='app.News', verbose_name='Новость')),
            ],
            options={
                'verbose_name_plural': 'Пиво к новости',
                'verbose_name': 'Пиво к новости',
            },
        ),
    ]
