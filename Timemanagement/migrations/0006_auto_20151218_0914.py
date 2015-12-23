# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0005_auto_20151218_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_timesheet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 9, 14, 47, 109201), editable=False),
        ),
    ]
