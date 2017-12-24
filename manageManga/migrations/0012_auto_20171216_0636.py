# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-16 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageManga', '0011_auto_20171216_0541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['slug'], 'verbose_name_plural': 'Chapters'},
        ),
        migrations.AlterField(
            model_name='manga',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
