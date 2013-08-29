# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.part_number'
        db.alter_column(u'products_product', 'part_number', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Product.sku'
        db.alter_column(u'products_product', 'sku', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Product.mpn'
        db.alter_column(u'products_product', 'mpn', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

    def backwards(self, orm):

        # Changing field 'Product.part_number'
        db.alter_column(u'products_product', 'part_number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Product.sku'
        db.alter_column(u'products_product', 'sku', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Product.mpn'
        db.alter_column(u'products_product', 'mpn', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

    models = {
        u'products.barcode': {
            'Meta': {'unique_together': "(('product', 'type'),)", 'object_name': 'Barcode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.BarcodeType']"})
        },
        u'products.barcodetype': {
            'Meta': {'object_name': 'BarcodeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'amazon_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'ean': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'height': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'isbn10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'jan': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'model_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'mpn': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'nsn': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'onemg': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'upc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'width': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['products']