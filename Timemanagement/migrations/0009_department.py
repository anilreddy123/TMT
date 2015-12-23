# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0008_auto_20151218_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=20, choices=[(b'Elearning', b'Elearning'), (b'software', b'Software'), (b'multimedia', b'Multimedia'), (b'qa', b'QA')])),
            ],
        ),
    ]
