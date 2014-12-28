# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20141226_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='long_content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='short_content',
        ),
    ]
