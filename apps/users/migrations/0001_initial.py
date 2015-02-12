# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import multiselectfield.db.fields
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=40)),
                ('student_number', models.CharField(unique=True, max_length=9)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('position', models.CharField(default=b'ME', max_length=2, choices=[(b'PR', b'President'), (b'VP', b'Vice-President'), (b'TR', b'Treasurer'), (b'SE', b'Secretary'), (b'VO', b'Vocal'), (b'ME', b'Member')])),
                ('phone_number', models.CharField(max_length=10, blank=True)),
                ('courses', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=169, choices=[(b'COTI-3101', b'Programming Fundamentals I'), (b'COTI-3102', b'Programming Fundamentals II'), (b'SICI-4036', b'Data Structures'), (b'COTI-4210', b'Web Applications'), (b'SICI-4030', b'Database'), (b'MATE-3171', b'Pre-Calculus I'), (b'MATE-3172', b'Pre-Calculus II'), (b'MATE-3175', b'Discrete Mathematics'), (b'MATE-3031', b'Calculus I'), (b'MATE-3032', b'Calculus II'), (b'MATE-3026', b'Statistics Using Computers'), (b'ESPA-3101', b'Basic Spanish I'), (b'ESPA-3102', b'Basic Spanish II'), (b'ESCO-4005', b'Tech. Report Writing In Spanish'), (b'INGL-3101', b'Basic English I'), (b'INGL-3102', b'Basic English II'), (b'INCO-4025', b'Tech. Report Writing In English')])),
                ('programming_languages', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=117, choices=[(b'cplusplus', b'C++'), (b'objc', b'Objective-C'), (b'python', b'Python'), (b'java', b'Java'), (b'c', b'C'), (b'scala', b'Scala'), (b'perl', b'Perl'), (b'ruby', b'Ruby'), (b'csharp', b'C#'), (b'php', b'php'), (b'html', b'HTML'), (b'css', b'CSS'), (b'javascript', b'JavaScript'), (b'grails', b'Grails'), (b'ruby-on-rails', b'Ruby on Rails'), (b'playframework', b'Play Framework'), (b'nodejs', b'Node.js')])),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_payed', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(None)])),
                ('year_payed', models.CharField(max_length=6, choices=[(b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020'), (b'2021', b'2021'), (b'2022', b'2022'), (b'2023', b'2023'), (b'2024', b'2024')])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('payed_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([('payed_by', 'year_payed')]),
        ),
    ]
