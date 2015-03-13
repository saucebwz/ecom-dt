# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0013_auto_20150313_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catalog',
            field=models.ManyToManyField(to='Bank.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 22, 35, 7, 534181, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
