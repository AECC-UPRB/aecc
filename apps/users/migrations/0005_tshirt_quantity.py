# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150218_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
