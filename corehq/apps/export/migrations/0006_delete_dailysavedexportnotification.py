# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-09 19:24
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0005_datafile_blobmeta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DailySavedExportNotification',
        ),
    ]
