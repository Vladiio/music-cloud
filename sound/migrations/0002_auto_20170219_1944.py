# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
