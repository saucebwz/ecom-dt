# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0002_auto_20150309_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankuser',
            name='money',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=True,
        ),
    ]
