# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('rating', models.CharField(default=b'Smash hit', max_length=10, choices=[(b'Smash hit', b'Smash hit'), (b'Must see', b'Must see'), (b'Worth a watch', b'Worth a watch'), (b'You might like it', b'You might like it'), (b'Avoid like the plague', b'Avoid like the plague')])),
                ('percentage', models.CharField(max_length=3, null=True, blank=True)),
                ('box_office', models.CharField(max_length=10, null=True, blank=True)),
                ('budget', models.CharField(max_length=10, null=True, blank=True)),
                ('opening_weekend', models.CharField(max_length=10, null=True, blank=True)),
                ('year', models.CharField(max_length=4, null=True, blank=True)),
                ('genre', models.CharField(default=b'Action', max_length=8, choices=[(b'Action', b'Action'), (b'Comedy', b'Comedy'), (b'Drama', b'Drama'), (b'Romance', b'Romance'), (b'Thriller', b'Thriller'), (b'Sci Fi', b'Sci Fi')])),
                ('alt_img', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
