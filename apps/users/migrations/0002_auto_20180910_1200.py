# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='code',
            field=models.CharField(max_length=6, verbose_name='\u9a8c\u8bc1\u7801'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='email',
            field=models.CharField(max_length=100, verbose_name='\u90ae\u7bb1'),
        ),
    ]
