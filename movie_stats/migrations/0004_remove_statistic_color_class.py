# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0003_auto_20170804_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='color_class',
        ),
    ]
