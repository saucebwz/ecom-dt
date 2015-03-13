# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankuser',
            name='money',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
