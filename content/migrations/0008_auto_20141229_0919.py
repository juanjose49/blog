# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20141228_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticcontent',
            name='title',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
