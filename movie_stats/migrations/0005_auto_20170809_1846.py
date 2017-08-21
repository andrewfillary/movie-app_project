# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0004_remove_statistic_color_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistic',
            old_name='image',
            new_name='cover_art',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='alt_img',
        ),
        migrations.AddField(
            model_name='statistic',
            name='actors',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='director',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='dvd_release',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='review',
            field=models.TextField(default='write review'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistic',
            name='screen_image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='theatre_release',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
