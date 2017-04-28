# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_auto_20151205_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='order',
        ),
    ]
