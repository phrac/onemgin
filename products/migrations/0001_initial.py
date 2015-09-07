# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'barcodes/ean13/')),
            ],
        ),
        migrations.CreateModel(
            name='BarcodeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('onemg', models.CharField(unique=True, max_length=13)),
                ('ean', models.CharField(unique=True, max_length=13)),
                ('upc', models.CharField(unique=True, max_length=12)),
                ('jan', models.CharField(max_length=13, null=True)),
                ('gtin', models.CharField(max_length=14, null=True)),
                ('nsn', models.CharField(max_length=14, null=True)),
                ('isbn10', models.CharField(max_length=10, null=True)),
                ('isbn13', models.CharField(max_length=13, null=True)),
                ('asin', models.CharField(max_length=10, null=True)),
                ('brand', models.CharField(max_length=128, null=True)),
                ('manufacturer', models.CharField(max_length=128, null=True)),
                ('mpn', models.CharField(max_length=64, null=True)),
                ('part_number', models.CharField(max_length=64, null=True)),
                ('sku', models.CharField(max_length=64, null=True)),
                ('model_number', models.CharField(max_length=64, null=True)),
                ('length', models.FloatField(null=True)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('description', models.CharField(max_length=512, null=True)),
                ('image_url', models.CharField(max_length=512, null=True)),
                ('amazon_url', models.URLField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='barcode',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='barcode',
            name='type',
            field=models.ForeignKey(to='products.BarcodeType'),
        ),
        migrations.AlterUniqueTogether(
            name='barcode',
            unique_together=set([('product', 'type')]),
        ),
    ]
