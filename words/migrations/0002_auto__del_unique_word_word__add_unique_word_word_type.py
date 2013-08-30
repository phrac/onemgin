# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Word', fields ['word']
        db.delete_unique(u'words_word', ['word'])

        # Adding unique constraint on 'Word', fields ['word', 'type']
        db.create_unique(u'words_word', ['word', 'type_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Word', fields ['word', 'type']
        db.delete_unique(u'words_word', ['word', 'type_id'])

        # Adding unique constraint on 'Word', fields ['word']
        db.create_unique(u'words_word', ['word'])


    models = {
        u'words.word': {
            'Meta': {'ordering': "['word']", 'unique_together': "(('word', 'type'),)", 'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['words.WordType']"}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'words.wordtype': {
            'Meta': {'object_name': 'WordType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['words']