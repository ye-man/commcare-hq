# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-28 21:10
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations

from corehq.apps.accounting.bootstrap.config.report_builder_v0 import BOOTSTRAP_CONFIG as report_builder_config
from corehq.apps.accounting.bootstrap.utils import ensure_plans
from corehq.sql_db.operations import HqRunPython


def _cchq_software_plan_update(apps, schema_editor):
    ensure_plans(report_builder_config, verbose=True, apps=apps)


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_practice_mobile_workers'),
    ]

    operations = [
        HqRunPython(_cchq_software_plan_update),
    ]
