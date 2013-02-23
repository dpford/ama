# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ama.created'
        db.add_column('qa_ama', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ama.created'
        db.delete_column('qa_ama', 'created')


    models = {
        'qa.ama': {
            'Meta': {'object_name': 'Ama'},
            'ama_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
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