# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0002_auto_20151217_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coursename', models.CharField(max_length=20)),
                ('clint', models.ForeignKey(to='Timemanagement.Clints')),
                ('projects', models.ForeignKey(to='Timemanagement.Projects')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
