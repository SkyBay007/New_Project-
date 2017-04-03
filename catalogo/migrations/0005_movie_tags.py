# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 16:19
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('catalogo', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
