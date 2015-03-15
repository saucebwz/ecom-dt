# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0022_auto_20150315_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 1, 8, 29, 437597, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
