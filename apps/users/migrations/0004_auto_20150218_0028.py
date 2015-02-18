# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150216_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('payment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='users.Payment')),
                ('size', models.CharField(max_length=3, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'X-Large'), (b'2XL', b'XX-Large'), (b'3XL', b'XXX-Large'), (b'S', b'Small'), (b'S', b'Small')])),
                ('back_name', models.CharField(max_length=40, blank=True)),
            ],
            options={
            },
            bases=('users.payment',),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount_payed',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='year_payed',
            field=models.CharField(max_length=6, choices=[(b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020'), (b'2021', b'2021'), (b'2022', b'2022'), (b'2023', b'2023'), (b'2024', b'2024')]),
            preserve_default=True,
        ),
    ]
