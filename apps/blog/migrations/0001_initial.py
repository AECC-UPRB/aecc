# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('article_slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='title')),
            ('branch_slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='branch')),
        ))
        db.send_create_signal(u'blog', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'blog_article')


    models = {
        u'blog.article': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Article'},
            'article_slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'title'"}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'branch_slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'branch'"}),
            'content': ('tinymce.models.HTMLField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'amount_payed': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'courses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '169', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'ME'", 'max_length': '2'}),
            'programming_languages': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '117', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'student_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']