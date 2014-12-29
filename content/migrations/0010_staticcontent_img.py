# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20141229_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticcontent',
            name='img',
            field=models.ImageField(upload_to='img/', default=''),
            preserve_default=False,
        ),
    ]
