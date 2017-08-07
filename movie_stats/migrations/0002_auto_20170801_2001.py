# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='box_office',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='budget',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='opening_weekend',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
