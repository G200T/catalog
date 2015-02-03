# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0015_auto_20150123_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.TextField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
    ]
