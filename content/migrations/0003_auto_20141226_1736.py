# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20141226_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='publication',
            name='short_content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
