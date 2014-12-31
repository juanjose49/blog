# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_staticcontent_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
