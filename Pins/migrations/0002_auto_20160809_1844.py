# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='created_on',
            field=models.DateField(auto_now_add=True, default='2016-8-9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pin',
            name='tagline',
            field=models.CharField(default='2016-8-9', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pin',
            name='updated_on',
            field=models.DateField(auto_now=True, default='2016-8-9'),
            preserve_default=False,
        ),
    ]
