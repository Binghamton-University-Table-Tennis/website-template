# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-18 05:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0046_auto_20170418_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slides',
            old_name='SlidesID',
            new_name='YouTube_ID',
        ),
    ]