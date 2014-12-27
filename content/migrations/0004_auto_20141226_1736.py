# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20141226_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubtype',
            name='type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staticcontent',
            name='purpose',
            field=models.CharField(max_length=200),
        ),
    ]
