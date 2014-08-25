# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.year_payed'
        db.add_column(u'users_user', 'year_payed',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.year_payed'
        db.delete_column(u'users_user', 'year_payed')


    models = {
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
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'year_payed': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        }
    }

    complete_apps = ['users']