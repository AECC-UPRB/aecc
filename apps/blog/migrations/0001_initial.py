# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import tinymce.models
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=25)),
                ('branch', models.CharField(max_length=12, choices=[(b'directive', b'Directive'), (b'hacknigths', b'Hacknigths'), (b'internships', b'Internships')])),
                ('content', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('article_slug', autoslug.fields.AutoSlugField(editable=False)),
                ('branch_slug', autoslug.fields.AutoSlugField(editable=False)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
    ]
