# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='depertment',
            new_name='department',
        ),
    ]
