# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 20:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_auto_20171004_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentpost',
            name='img_on',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='commentpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 23, 55, 32, 374505), verbose_name='Дата комментария'),
        ),
    ]
