# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clintname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectname', models.CharField(max_length=20)),
                ('clint', models.ForeignKey(to='Timemanagement.Clints')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('depertment', models.CharField(max_length=2, choices=[(b'Elearning', b'Elearning'), (b'software', b'Software'), (b'multimedia', b'Multimedia'), (b'qa', b'QA')])),
            ],
        ),
    ]
