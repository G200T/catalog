# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0021_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='url',
        ),
    ]
