# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import taggit.managers
from django.conf import settings
import apps.events.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('month', models.CharField(max_length=10, choices=[(b'january', b'january'), (b'february', b'february'), (b'march', b'march'), (b'april', b'april'), (b'may', b'may'), (b'june', b'june'), (b'july', b'july'), (b'august', b'august'), (b'september', b'september'), (b'october', b'october'), (b'november', b'november'), (b'december', b'december')])),
                ('event_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('promo_picture', models.FileField(upload_to=apps.events.models.get_upload_file_name, blank=True)),
                ('title_slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('month_slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('checked_in', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-event_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('picture', models.FileField(upload_to=apps.events.models.get_upload_file_name, blank=True)),
                ('website', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
