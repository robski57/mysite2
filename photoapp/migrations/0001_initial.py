# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-06 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='searchTwitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_list', models.CharField(max_length=200)),
                ('article', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='searchtwitter',
            name='tweets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoapp.summary'),
        ),
    ]
