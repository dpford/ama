# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ama'
        db.create_table('qa_ama', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('ama_id', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('orig_poster', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('qa', ['Ama'])

        # Adding model 'Qa'
        db.create_table('qa_qa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qa.Ama'])),
            ('ups', self.gf('django.db.models.fields.IntegerField')(max_length=7)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('asker', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('qa', ['Qa'])


    def backwards(self, orm):
        # Deleting model 'Ama'
        db.delete_table('qa_ama')

        # Deleting model 'Qa'
        db.delete_table('qa_qa')


    models = {
        'qa.ama': {
            'Meta': {'object_name': 'Ama'},
            'ama_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orig_poster': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'qa.qa': {
            'Meta': {'object_name': 'Qa'},
            'ama': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['qa.Ama']"}),
            'answer': ('django.db.models.fields.TextField', [], {}),
            'asker': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'ups': ('django.db.models.fields.IntegerField', [], {'max_length': '7'})
        }
    }

    complete_apps = ['qa']