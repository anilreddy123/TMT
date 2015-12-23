# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0004_auto_20151217_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Timesheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now, editable=False)),
                ('task_description', models.CharField(max_length=50)),
                ('task_type', models.CharField(max_length=20, choices=[(b'Fresh', b'FRESH'), (b'Change Order', b'CHANGE ORDER')])),
                ('effort_hours', models.CharField(max_length=10, choices=[(b'0', b'00'), (b'1', b'01'), (b'2', b'02'), (b'3', b'03'), (b'4', b'04'), (b'5', b'05'), (b'6', b'06'), (b'7', b'07'), (b'8', b'08'), (b'9', b'09')])),
                ('effort_minutes', models.CharField(max_length=10, choices=[(b'00', b'00'), (b'25', b'25'), (b'50', b'50'), (b'75', b'75'), (b'100', b'100')])),
                ('client', models.ForeignKey(to='Timemanagement.Clints')),
                ('course', models.ForeignKey(to='Timemanagement.Courses')),
                ('project', models.ForeignKey(to='Timemanagement.Projects')),
            ],
        ),
        migrations.RemoveField(
            model_name='user_panel',
            name='clint',
        ),
        migrations.RemoveField(
            model_name='user_panel',
            name='course',
        ),
        migrations.RemoveField(
            model_name='user_panel',
            name='project',
        ),
        migrations.DeleteModel(
            name='User_Panel',
        ),
    ]
