# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


NOOP = 'SELECT 1'


def _alter_to_uuid_sql_forawd(model, field):
    return 'ALTER TABLE "form_processor_{model}" ALTER COLUMN "{field}" TYPE uuid USING {field}::uuid'.format(
        model=model, field=field
    )


def _alter_to_uuid_sql_reverse(model, field):
    return 'ALTER TABLE "form_processor_{model}" ALTER COLUMN "{field}" TYPE varchar(255)'.format(
        model=model, field=field
    )


def migrate_field_to_uuid(model, field, unique=True, db_index=True, null=False):
    forward = _alter_to_uuid_sql_forawd(model, field)
    reverse = _alter_to_uuid_sql_reverse(model, field)

    return migrations.RunSQL(
        forward,
        reverse,
        state_operations=[migrations.AlterField(
            model_name=model,
            name=field,
            field=uuidfield.fields.UUIDField(
                unique=unique,
                max_length=32,
                db_index=db_index,
                null=null),
            preserve_default=True,
        )]
    )


class Migration(migrations.Migration):

    dependencies = [
        ('form_processor', '0035_remove_varchar_pattern_ops_indexes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xformattachmentsql',
            old_name='xform',
            new_name='form',
        ),
        migrations.RenameField(
            model_name='xformoperationsql',
            old_name='xform',
            new_name='form',
        ),
        migrations.RenameField(
            model_name='xforminstancesql',
            old_name='form_uuid',
            new_name='form_id',
        ),
        # workaround for https://code.djangoproject.com/ticket/25817
        # but another bug prevents squashing: https://code.djangoproject.com/ticket/25818
        migrations.RunSQL(
            NOOP, NOOP,
            state_operations=[
                migrations.AlterField(
                    model_name='xformattachmentsql',
                    name='form',
                    field=models.ForeignKey(related_query_name=b'attachment', related_name='attachments', to_field=b'form_id', to='form_processor.XFormInstanceSQL'),
                    preserve_default=True,
                ),
                migrations.AlterField(
                    model_name='xformoperationsql',
                    name='form',
                    field=models.ForeignKey(to='form_processor.XFormInstanceSQL', to_field=b'form_id'),
                    preserve_default=True,
                ),
            ]
        ),
        migrations.AlterField(
            model_name='caseattachmentsql',
            name='case',
            field=models.ForeignKey(related_query_name=b'attachment', related_name='attachments', to_field=b'case_uuid', to='form_processor.CommCareCaseSQL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casetransaction',
            name='case',
            field=models.ForeignKey(related_query_name=b'transaction', related_name='transaction_set', to_field=b'case_uuid', to='form_processor.CommCareCaseSQL', db_index=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commcarecaseindexsql',
            name='case',
            field=models.ForeignKey(related_query_name=b'index', related_name='index_set', to_field=b'case_uuid', to='form_processor.CommCareCaseSQL'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='casetransaction',
            old_name='form_uuid',
            new_name='form_id',
        ),
        migrations.AlterUniqueTogether(
            name='casetransaction',
            unique_together=set([('case', 'form_id')]),
        ),
        migrations.RenameField(
            model_name='commcarecasesql',
            old_name='case_uuid',
            new_name='case_id',
        ),
        # workaround for https://code.djangoproject.com/ticket/25817
        # but another bug prevents squashing: https://code.djangoproject.com/ticket/25818
        migrations.RunSQL(
            NOOP, NOOP,
            state_operations=[
                migrations.AlterField(
                    model_name='caseattachmentsql',
                    name='case',
                    field=models.ForeignKey(related_query_name=b'attachment', related_name='attachments', to_field=b'case_id', to='form_processor.CommCareCaseSQL'),
                    preserve_default=True,
                ),
                migrations.AlterField(
                    model_name='casetransaction',
                    name='case',
                    field=models.ForeignKey(related_query_name=b'transaction', related_name='transaction_set', to_field=b'case_id', to='form_processor.CommCareCaseSQL', db_index=False),
                    preserve_default=True,
                ),
                migrations.AlterField(
                    model_name='commcarecaseindexsql',
                    name='case',
                    field=models.ForeignKey(related_query_name=b'index', related_name='index_set', to_field=b'case_id', to='form_processor.CommCareCaseSQL'),
                    preserve_default=True,
                ),
            ]
        ),
        migrations.AlterField(
            model_name='caseattachmentsql',
            name='case',
            field=models.ForeignKey(related_query_name=b'attachment', related_name='attachment_set', to_field=b'case_id', to='form_processor.CommCareCaseSQL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='xformattachmentsql',
            name='form',
            field=models.ForeignKey(related_query_name=b'attachment', related_name='attachment_set', to_field=b'form_id', to='form_processor.XFormInstanceSQL'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='xformoperationsql',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='commcarecasesql',
            old_name='location_uuid',
            new_name='location_id',
        ),
        # custom migration in order to support backwards migration
        migrations.RunSQL(
            'ALTER TABLE form_processor_commcarecasesql ALTER COLUMN "location_id" TYPE varchar(255)',
            'ALTER TABLE form_processor_commcarecasesql ALTER COLUMN "location_id" TYPE uuid USING location_id::uuid',
            state_operations=[
                migrations.AlterField(
                    model_name='commcarecasesql',
                    name='location_id',
                    field=models.CharField(max_length=255, null=True),
                    preserve_default=True,
                ),
            ]
        ),
        migrations.RenameField(
            model_name='caseattachmentsql',
            old_name='attachment_uuid',
            new_name='attachment_id',
        ),
        migrations.RenameField(
            model_name='xformattachmentsql',
            old_name='attachment_uuid',
            new_name='attachment_id',
        ),
        migrate_field_to_uuid('caseattachmentsql', 'attachment_id'),
        migrate_field_to_uuid('xformattachmentsql', 'attachment_id'),
        migrations.AlterField(
            model_name='casetransaction',
            name='case',
            field=models.ForeignKey(related_query_name=b'transaction', related_name='transaction_set', to_field=b'case_id', to='form_processor.CommCareCaseSQL'),
            preserve_default=True,
        ),
    ]
