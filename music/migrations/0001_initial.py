# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WangyiMusic',
            fields=[
                ('sm_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('cat', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('comnum', models.IntegerField(default=0)),
                ('pnum', models.IntegerField(default=0)),
                ('colnum', models.IntegerField(default=0)),
                ('shnum', models.IntegerField(default=0)),
                ('ctime', models.CharField(max_length=50)),
            ],
        ),
    ]
