# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalog.ctlg.Thumbnail


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0017_auto_20150127_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='image',
            field=catalog.ctlg.Thumbnail.ThumbnailImageField(null=True, upload_to=b'photos'),
            preserve_default=True,
        ),
    ]
