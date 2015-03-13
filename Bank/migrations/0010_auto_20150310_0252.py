# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('Bank', '0009_auto_20150310_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybankuser',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', verbose_name='groups', to='auth.Group', blank=True, related_query_name='user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mybankuser',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mybankuser',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', to='auth.Permission', blank=True, related_query_name='user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybankuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 23, 52, 35, 77556, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
