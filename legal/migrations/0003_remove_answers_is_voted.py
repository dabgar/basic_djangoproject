# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-31 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0002_answers_is_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='is_voted',
        ),
    ]
