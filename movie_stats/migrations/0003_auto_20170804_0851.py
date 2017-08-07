# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0002_auto_20170801_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='color_class',
            field=models.CharField(default=b'Green', max_length=6, choices=[(b'Green', b'Green'), (b'Orange', b'Orange'), (b'Red', b'Red')]),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='rating',
            field=models.CharField(default=b'Smash hit', max_length=15, choices=[(b'Must see', b'Must see'), (b'Worth a watch', b'Worth a watch'), (b'B Movie', b'B Movie')]),
        ),
    ]
