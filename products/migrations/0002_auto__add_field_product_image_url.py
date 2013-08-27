# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.image_url'
        db.add_column(u'products_product', 'image_url',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.image_url'
        db.delete_column(u'products_product', 'image_url')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'ean': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '13'}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'isbn10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'jan': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'nsn': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'onemg': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'upc': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '12'})
        }
    }

    complete_apps = ['products']