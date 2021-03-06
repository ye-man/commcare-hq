# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 14:56
from __future__ import absolute_import, unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0114_local_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitusDashboardDiff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('data_source', models.TextField()),
                ('context', django.contrib.postgres.fields.jsonb.JSONField()),
                ('control', django.contrib.postgres.fields.jsonb.JSONField()),
                ('candidate', django.contrib.postgres.fields.jsonb.JSONField()),
                ('diff', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='CitusDashboardException',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('data_source', models.TextField()),
                ('context', django.contrib.postgres.fields.jsonb.JSONField()),
                ('exception', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CitusDashboardTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('data_source', models.TextField()),
                ('context', django.contrib.postgres.fields.jsonb.JSONField()),
                ('control_duration', models.DecimalField(decimal_places=3, max_digits=10)),
                ('candidate_duration', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
