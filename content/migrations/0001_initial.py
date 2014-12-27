# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(default='')),
                ('short_content', models.TextField(default='')),
                ('long_content', models.TextField(default='')),
                ('img', models.FilePathField(path=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaticContent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('purpose', models.TextField(default='')),
                ('content', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.ForeignKey(to='content.PubType', default=None),
            preserve_default=True,
        ),
    ]
