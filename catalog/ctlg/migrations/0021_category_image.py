# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalog.ctlg.Thumbnail


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0020_unit_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=catalog.ctlg.Thumbnail.ThumbnailImageField(null=True, upload_to=b'photos'),
            preserve_default=True,
        ),
    ]
