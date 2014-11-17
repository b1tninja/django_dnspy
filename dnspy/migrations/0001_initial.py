# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('parent', models.BigIntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'names',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('requested', models.DateTimeField()),
                ('completed', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'queries',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('type', models.IntegerField()),
                ('qclass', models.IntegerField(db_column='class')),
            ],
            options={
                'db_table': 'questions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('type', models.IntegerField()),
                ('rclass', models.IntegerField(db_column='class')),
                ('ttl', models.IntegerField()),
                ('rdata', models.BinaryField(blank=True)),
                ('cached', models.DateTimeField()),
            ],
            options={
                'db_table': 'records',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
