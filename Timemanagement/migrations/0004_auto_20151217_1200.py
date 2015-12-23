# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0003_auto_20151217_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('task_description', models.CharField(max_length=40)),
                ('task_type', models.CharField(max_length=2, choices=[(b'fresh', b'Fresh'), (b'change order', b'Change Order')])),
                ('effort', models.CharField(max_length=2, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8')])),
                ('clint', models.ForeignKey(to='Timemanagement.Clints')),
            ],
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='projects',
            new_name='project',
        ),
        migrations.AddField(
            model_name='user_panel',
            name='course',
            field=models.ForeignKey(to='Timemanagement.Courses'),
        ),
        migrations.AddField(
            model_name='user_panel',
            name='project',
            field=models.ForeignKey(to='Timemanagement.Projects'),
        ),
    ]
