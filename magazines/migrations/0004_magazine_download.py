# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0003_magazine_alt_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='download',
            field=models.FileField(null=True, upload_to=b'files', blank=True),
        ),
    ]
