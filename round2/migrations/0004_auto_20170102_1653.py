# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round2', '0003_question_correct_op'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='college_name1',
        ),
        migrations.AddField(
            model_name='user',
            name='attempted_answers',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='attempted_questions',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='college_name2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='correct_answered',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='user',
            name='count_easy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='count_hard',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='count_medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='email1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='end_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='question_array_easy',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='question_array_hard',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='question_array_medium',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='user_bonus_activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_bonus_clicked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_name2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
