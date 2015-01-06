# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20150103_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='short_content',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
