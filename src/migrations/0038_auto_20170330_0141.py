# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-30 05:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0037_auto_20170330_0017'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClubAttendance',
        ),
        migrations.AddField(
            model_name='attendancehistory',
            name='Time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 30, 5, 41, 41, 179315, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=False,
        ),
    ]
