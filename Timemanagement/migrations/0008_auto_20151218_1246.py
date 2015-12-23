# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0007_auto_20151218_0915'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clints',
            new_name='Clients',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='clintname',
            new_name='clientname',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='clint',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='clint',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='date',
            field=models.DateField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='effort_hours',
            field=models.CharField(max_length=10, choices=[(b'0', b'00'), (b'1', b'01'), (b'2', b'02'), (b'3', b'03 '), (b'4', b'04'), (b'5', b'05 '), (b'6', b'06'), (b'7', b'07'), (b'8', b'08'), (b'9', b'09')]),
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='effort_minutes',
            field=models.CharField(max_length=10, choices=[(b'00', b'00 m'), (b'25', b'25 m'), (b'50', b'50 m'), (b'75', b'75 m'), (b'100', b'100 m')]),
        ),
    ]
