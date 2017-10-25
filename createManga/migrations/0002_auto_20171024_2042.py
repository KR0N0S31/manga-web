# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 01:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('createManga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'verbose_name_plural': 'Mangas'},
        ),
        migrations.AddField(
            model_name='manga',
            name='state',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentarios',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createManga.Manga'),
        ),
    ]
