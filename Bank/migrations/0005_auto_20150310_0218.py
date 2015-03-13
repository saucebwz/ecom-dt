# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0004_bankuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBankUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=40, db_index=True)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('second_name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2015, 3, 9, 23, 18, 21, 445095, tzinfo=utc))),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bankuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='BankUser',
        ),
    ]
