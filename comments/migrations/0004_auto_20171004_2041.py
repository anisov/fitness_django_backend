# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 17:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20171003_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('vk_url', models.URLField(max_length=250, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Фото')),
                ('text', models.TextField(null=True, verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2017, 10, 4, 20, 41, 2, 639732), verbose_name='Дата комментария')),
                ('approved_comment', models.BooleanField(default=True)),
                ('ip_address', models.GenericIPAddressField(default='127.1.0.1', verbose_name='ip')),
            ],
            options={
                'verbose_name': 'Коментарии',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.DeleteModel(
            name='Comment_post',
        ),
    ]
