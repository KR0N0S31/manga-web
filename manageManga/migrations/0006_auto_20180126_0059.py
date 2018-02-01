# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-26 00:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageManga', '0005_auto_20180125_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='image',
            field=models.ImageField(default=1, upload_to='manga/portadas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manga',
            name='description',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Description'),
        ),
    ]