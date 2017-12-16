# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round2', '0004_auto_20170102_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='attempted_answers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='attempted_questions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='correct_answered',
        ),
        migrations.RemoveField(
            model_name='user',
            name='count_easy',
        ),
        migrations.RemoveField(
            model_name='user',
            name='count_hard',
        ),
        migrations.RemoveField(
            model_name='user',
            name='count_medium',
        ),
        migrations.RemoveField(
            model_name='user',
            name='level',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question_array_easy',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question_array_hard',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question_array_medium',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_bonus_activated',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_bonus_clicked',
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.TextField(default=0),
        ),
    ]
