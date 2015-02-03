# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0004_auto_20150122_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub',
            field=models.ForeignKey(related_name='categ', blank=True, to='ctlg.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='sub',
            field=models.ForeignKey(related_name='units', to='ctlg.Category'),
            preserve_default=True,
        ),
    ]
