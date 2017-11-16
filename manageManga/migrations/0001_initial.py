# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 21:00
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import manageManga.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to=manageManga.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.IntegerField(choices=[(1, 'Acción'), (2, 'Apocalíptico'), (3, 'Artes Marciales'), (4, 'Aventura'), (5, 'Ciencia Ficción'), (6, 'Comedia'), (7, 'Cyberpunk'), (8, 'Demonios'), (9, 'Deportes'), (10, 'Drama'), (11, 'Ecchi'), (12, 'Fantasía'), (13, 'Gender Bender'), (14, 'Gore'), (15, 'Harem'), (16, 'Histórico'), (17, 'Horror'), (18, 'Magia'), (19, 'Mecha'), (20, 'Militar'), (21, 'Misterio'), (22, 'Musical'), (23, 'Parodia'), (24, 'Policial'), (25, 'Psicológico'), (26, 'Realidad Virtual'), (27, 'Recuentos de la vida'), (28, 'Reencarnación'), (29, 'Romance'), (30, 'Samurai'), (31, 'Sobrenatural'), (32, 'Super Poderes'), (33, 'Supervivencia'), (34, 'Suspense'), (35, 'Tragedia'), (36, 'Vampiros'), (37, 'Vida Escolar'), (38, 'Yaoi'), (39, 'Yuri')], unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(39)])),
                ('name', models.CharField(default='DEFAULT', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=700, verbose_name='Description')),
                ('published_date', models.DateField(auto_now_add=True, verbose_name='Published Date')),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, verbose_name='Slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('genres', models.ManyToManyField(to='manageManga.Genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name_plural': 'Mangas',
                'ordering': ['published_date'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'Emision'), (2, 'Finalizado'), (3, 'Pausado'), (4, 'Cancelado')], unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('name', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='manga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageManga.State', verbose_name='State'),
        ),
        migrations.AddField(
            model_name='comment',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageManga.Manga'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageManga.Manga'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
