# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0017_auto_20150314_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 22, 28, 34, 953665, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/images/', default='no', blank=True),
            preserve_default=True,
        ),
    ]
