# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-12 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round2', '0013_user_buyed_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
