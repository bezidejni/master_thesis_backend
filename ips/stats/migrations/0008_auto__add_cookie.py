# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cookie'
        db.create_table(u'stats_cookie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('secure', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('http_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'stats', ['Cookie'])


    def backwards(self, orm):
        # Deleting model 'Cookie'
        db.delete_table(u'stats_cookie')


    models = {
        u'stats.cookie': {
            'Meta': {'object_name': 'Cookie'},
            'domain': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'http_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'secure': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'stats.cpuinfo': {
            'Meta': {'object_name': 'CPUInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'})
        },
        u'stats.domelementcount': {
            'Meta': {'object_name': 'DOMElementCount'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'element_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'stats.networkinfo': {
            'Meta': {'object_name': 'NetworkInfo'},
            'destination_url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'}),
            'http_status': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'GET'", 'max_length': '10'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'main_frame'", 'max_length': '15'})
        }
    }

    complete_apps = ['stats']