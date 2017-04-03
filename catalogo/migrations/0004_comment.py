# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0003_auto_20170324_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datee', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=500)),
                ('movie_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_movie', to='catalogo.Movie')),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('datee',),
            },
        ),
    ]
