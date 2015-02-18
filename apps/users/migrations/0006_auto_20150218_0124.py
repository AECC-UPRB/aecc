# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_tshirt_quantity'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([]),
        ),
    ]
