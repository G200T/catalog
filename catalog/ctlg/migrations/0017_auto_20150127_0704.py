# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0016_category_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='image',
            field=models.ImageField(null=True, upload_to=b'photos'),
            preserve_default=True,
        ),
    ]
