# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0016_auto_20160124_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='photo',
            field=models.ImageField(default=b'images/level1.jpg', upload_to=b'images/'),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 24, 20, 51, 37, 843788)),
        ),
    ]
