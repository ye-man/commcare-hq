# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 22:14
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0029_daily_outbound_sms_limit_reached'),
    ]

    operations = [
        migrations.CreateModel(
            name='KarixBackend',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('sms.sqlsmsbackend',),
        ),
    ]
