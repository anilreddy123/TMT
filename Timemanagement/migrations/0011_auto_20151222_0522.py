# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timemanagement', '0010_user_timesheet_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='client',
            field=models.ForeignKey(related_name='projectsunderclint', to='Timemanagement.Clients'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courses',
            name='project',
            field=models.ForeignKey(related_name='coursesunderprojects', to='Timemanagement.Projects'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projects',
            name='client',
            field=models.ForeignKey(related_name='projects_clint', to='Timemanagement.Clients'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='department',
            field=models.CharField(default=b'software', max_length=20, null=True, choices=[(b'Elearning', b'Elearning'), (b'software', b'Software'), (b'multimedia', b'Multimedia'), (b'qa', b'QA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='effort_hours',
            field=models.CharField(default=b'0', max_length=10, choices=[(b'0', b'00'), (b'1', b'01'), (b'2', b'02'), (b'3', b'03 '), (b'4', b'04'), (b'5', b'05 '), (b'6', b'06'), (b'7', b'07'), (b'8', b'08'), (b'9', b'09')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='effort_minutes',
            field=models.CharField(default=b'00', max_length=10, choices=[(b'00', b'00 m'), (b'25', b'25 m'), (b'50', b'50 m'), (b'75', b'75 m'), (b'100', b'100 m')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_timesheet',
            name='task_type',
            field=models.CharField(default=b'Fresh', max_length=20, choices=[(b'Fresh', b'FRESH'), (b'Change Order', b'CHANGE ORDER')]),
            preserve_default=True,
        ),
    ]
