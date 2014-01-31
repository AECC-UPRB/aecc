# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'People'
        db.create_table(u'people_people', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('picture', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'people', ['People'])


    def backwards(self, orm):
        # Deleting model 'People'
        db.delete_table(u'people_people')


    models = {
        u'people.people': {
            'Meta': {'object_name': 'People'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['people']