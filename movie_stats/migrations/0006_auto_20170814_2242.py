# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0005_auto_20170809_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('review', models.TextField()),
                ('cover_art', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('screen_image', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('rating', models.CharField(default=b'Smash hit', max_length=15, choices=[(b'Must see', b'Must see'), (b'Worth a watch', b'Worth a watch'), (b'B Movie', b'B Movie')])),
                ('percentage', models.CharField(max_length=3, null=True, blank=True)),
                ('box_office', models.CharField(max_length=15, null=True, blank=True)),
                ('budget', models.CharField(max_length=15, null=True, blank=True)),
                ('opening_weekend', models.CharField(max_length=15, null=True, blank=True)),
                ('director', models.CharField(max_length=20, null=True, blank=True)),
                ('actors', models.CharField(max_length=100, null=True, blank=True)),
                ('theatre_release', models.CharField(max_length=10, null=True, blank=True)),
                ('dvd_release', models.CharField(max_length=10, null=True, blank=True)),
                ('year', models.CharField(max_length=4, null=True, blank=True)),
                ('genre', models.CharField(default=b'Action', max_length=8, choices=[(b'Action', b'Action'), (b'Comedy', b'Comedy'), (b'Drama', b'Drama'), (b'Romance', b'Romance'), (b'Thriller', b'Thriller'), (b'Sci Fi', b'Sci Fi')])),
            ],
        ),
        migrations.DeleteModel(
            name='Statistic',
        ),
    ]
