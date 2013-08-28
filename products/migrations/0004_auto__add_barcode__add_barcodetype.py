# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Barcode'
        db.create_table(u'products_barcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.BarcodeType'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'products', ['Barcode'])

        # Adding model 'BarcodeType'
        db.create_table(u'products_barcodetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'products', ['BarcodeType'])

        # Adding M2M table for field barcodes on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_barcodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('barcode', models.ForeignKey(orm[u'products.barcode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'barcode_id'])


    def backwards(self, orm):
        # Deleting model 'Barcode'
        db.delete_table(u'products_barcode')

        # Deleting model 'BarcodeType'
        db.delete_table(u'products_barcodetype')

        # Removing M2M table for field barcodes on 'Product'
        db.delete_table(db.shorten_name(u'products_product_barcodes'))


    models = {
        u'products.barcode': {
            'Meta': {'object_name': 'Barcode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.BarcodeType']"})
        },
        u'products.barcodetype': {
            'Meta': {'object_name': 'BarcodeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'barcodes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'product_barcodes'", 'symmetrical': 'False', 'to': u"orm['products.Barcode']"}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'ean': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'isbn10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'jan': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'nsn': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'onemg': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'upc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'})
        }
    }

    complete_apps = ['products']