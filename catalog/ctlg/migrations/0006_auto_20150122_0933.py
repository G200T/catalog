# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0005_auto_20150122_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub',
            field=models.ForeignKey(related_name='categories', blank=True, to='ctlg.Category', null=True),
            preserve_default=True,
        ),
    ]
