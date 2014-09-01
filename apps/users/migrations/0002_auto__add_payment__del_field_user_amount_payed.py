# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'users_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('amount_payed', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('year_payed', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['Payment'])

        # Deleting field 'User.amount_payed'
        db.delete_column(u'users_user', 'amount_payed')


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'users_payment')

        # Adding field 'User.amount_payed'
        db.add_column(u'users_user', 'amount_payed',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    models = {
        u'users.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount_payed': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'year_payed': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
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

    complete_apps = ['users']