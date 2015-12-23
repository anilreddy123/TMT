# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0006_auto_20151218_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_timesheet',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 18, 9, 15, 33, 616017), editable=False),
        ),
    ]
