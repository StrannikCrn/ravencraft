# Generated by Django 2.0.7 on 2018-07-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20180710_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='beergroup',
            name='description',
            field=models.CharField(default='', max_length=255, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='beergroup',
            name='keywords',
            field=models.CharField(default='', max_length=255, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='beergroup',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Тайтл'),
        ),
    ]