# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20141229_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='image',
        ),
        migrations.AlterField(
            model_name='publication',
            name='img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
