# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0008_auto_20150122_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='slug',
            field=models.SlugField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),

    ]
