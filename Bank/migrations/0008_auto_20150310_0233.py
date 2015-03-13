# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0007_auto_20150310_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 23, 33, 54, 320452, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
