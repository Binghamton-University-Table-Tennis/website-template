# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-08 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20161007_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='Loser_Score',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)]),
        ),
        migrations.AlterField(
            model_name='matches',
            name='Winner_Score',
            field=models.IntegerField(choices=[(2, 2)]),
        ),
    ]
