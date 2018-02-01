# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 23:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageManga', '0003_auto_20180115_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='description',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Title'),
        ),
    ]