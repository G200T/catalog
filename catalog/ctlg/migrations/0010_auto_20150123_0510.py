# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from catalog.ctlg.models import Category, Unit


def add_slug(apps, schema_editor):
    for cat in Category.objects.all():
        cat.save()

    for unit in Unit.objects.all():
        unit.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ctlg', '0009_auto_20150123_0500'),
    ]

    operations = [
        migrations.RunPython(add_slug)
    ]
