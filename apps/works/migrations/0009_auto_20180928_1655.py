# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0008_auto_20180928_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admet',
            name='username',
        ),
        migrations.RemoveField(
            model_name='autoduck',
            name='username',
        ),
        migrations.RemoveField(
            model_name='autoduck2',
            name='username',
        ),
        migrations.RemoveField(
            model_name='dynamic',
            name='username',
        ),
        migrations.RemoveField(
            model_name='reversevirtualscreen',
            name='username',
        ),
        migrations.RemoveField(
            model_name='virtualscreen',
            name='username',
        ),
        migrations.RemoveField(
            model_name='virtualscreen2',
            name='username',
        ),
        migrations.RemoveField(
            model_name='vsblast',
            name='username',
        ),
    ]
