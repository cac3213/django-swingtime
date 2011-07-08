# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Note'
        db.create_table('swingtime_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('swingtime', ['Note'])

        # Adding model 'EventType'
        db.create_table('swingtime_eventtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swingtime', ['EventType'])

        # Adding model 'Event'
        db.create_table('swingtime_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('event_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swingtime.EventType'])),
        ))
        db.send_create_signal('swingtime', ['Event'])

        # Adding model 'Occurrence'
        db.create_table('swingtime_occurrence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swingtime.Event'])),
        ))
        db.send_create_signal('swingtime', ['Occurrence'])


    def backwards(self, orm):
        
        # Deleting model 'Note'
        db.delete_table('swingtime_note')

        # Deleting model 'EventType'
        db.delete_table('swingtime_eventtype')

        # Deleting model 'Event'
        db.delete_table('swingtime_event')

        # Deleting model 'Occurrence'
        db.delete_table('swingtime_occurrence')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'swingtime.event': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swingtime.EventType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'swingtime.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swingtime.note': {
            'Meta': {'object_name': 'Note'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'swingtime.occurrence': {
            'Meta': {'ordering': "('start_time', 'end_time')", 'object_name': 'Occurrence'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swingtime.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['swingtime']
