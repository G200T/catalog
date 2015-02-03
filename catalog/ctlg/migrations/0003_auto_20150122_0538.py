# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0002_category_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub',
            field=models.ForeignKey(blank=True, to='ctlg.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='image',
            field=models.ImageField(upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
    ]
