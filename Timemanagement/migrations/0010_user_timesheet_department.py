# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0009_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_timesheet',
            name='department',
            field=models.CharField(max_length=20, null=True, choices=[(b'Elearning', b'Elearning'), (b'software', b'Software'), (b'multimedia', b'Multimedia'), (b'qa', b'QA')]),
        ),
    ]
