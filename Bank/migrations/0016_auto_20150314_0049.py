# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0015_auto_20150313_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media_images/', default='no'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 21, 49, 42, 816274, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
