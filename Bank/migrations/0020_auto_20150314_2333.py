# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0019_auto_20150314_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='No description', max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 20, 33, 36, 768249, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
