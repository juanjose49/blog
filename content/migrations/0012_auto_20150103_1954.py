# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20141231_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
