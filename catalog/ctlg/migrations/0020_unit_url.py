# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0019_auto_20150128_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='url',
            field=models.TextField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
    ]
