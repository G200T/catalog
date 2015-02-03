# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalog.ctlg.Thumbnail


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0018_auto_20150128_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='image',
            field=catalog.ctlg.Thumbnail.ThumbnailImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
    ]
