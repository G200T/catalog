# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0006_auto_20150122_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='sub',
            field=models.ForeignKey(to='ctlg.Category'),
            preserve_default=True,
        ),
    ]
