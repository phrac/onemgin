# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Word', fields ['word', 'type']
        db.delete_unique(u'words_word', ['word', 'type_id'])

        # Deleting model 'WordType'
        db.delete_table(u'words_wordtype')

        # Deleting field 'Word.type'
        db.delete_column(u'words_word', 'type_id')

        # Adding unique constraint on 'Word', fields ['word']
        db.create_unique(u'words_word', ['word'])


    def backwards(self, orm):
        # Removing unique constraint on 'Word', fields ['word']
        db.delete_unique(u'words_word', ['word'])

        # Adding model 'WordType'
        db.create_table(u'words_wordtype', (
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'words', ['WordType'])

        # Adding field 'Word.type'
        db.add_column(u'words_word', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='poo', to=orm['words.WordType']),
                      keep_default=False)

        # Adding unique constraint on 'Word', fields ['word', 'type']
        db.create_unique(u'words_word', ['word', 'type_id'])


    models = {
        u'words.word': {
            'Meta': {'ordering': "['word']", 'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        }
    }

    complete_apps = ['words']