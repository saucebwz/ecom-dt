# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0018_auto_20150314_0128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories', 'ordering': ['-is_first']},
        ),
        migrations.AddField(
            model_name='category',
            name='is_first',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 20, 4, 57, 702924, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
