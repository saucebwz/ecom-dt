# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_auto_20150309_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankuser',
            name='username',
            field=models.CharField(default='', blank=True, max_length=20),
            preserve_default=True,
        ),
    ]
