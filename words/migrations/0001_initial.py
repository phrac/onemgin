# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table(u'words_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['words.WordType'])),
        ))
        db.send_create_signal(u'words', ['Word'])

        # Adding model 'WordType'
        db.create_table(u'words_wordtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'words', ['WordType'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table(u'words_word')

        # Deleting model 'WordType'
        db.delete_table(u'words_wordtype')


    models = {
        u'words.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['words.WordType']"}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        u'words.wordtype': {
            'Meta': {'object_name': 'WordType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['words']