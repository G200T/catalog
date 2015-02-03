# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub',
            field=models.ForeignKey(to='ctlg.Category', null=True),
            preserve_default=True,
        ),
    ]
