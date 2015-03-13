# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0008_auto_20150310_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 23, 37, 38, 505275, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybankuser',
            name='username',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
