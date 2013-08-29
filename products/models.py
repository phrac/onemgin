from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from elaphe import barcode
from StringIO import StringIO
import random
import string

def onemg_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

def barcode_file_name(instance, filename):
    import os
    name, ext = os.path.splitext(filename)
    path = 'documents/%s%s' % (str(instance.uuid), ext)
    return path

class Product(models.Model):
    onemg = models.CharField(max_length=13, unique=True)
    ean = models.CharField(max_length=13, unique=True)
    upc = models.CharField(max_length=12, unique=True)
    jan = models.CharField(max_length=13, null=True)
    gtin = models.CharField(max_length=14, null=True)
    nsn = models.CharField(max_length=14, null=True)
    isbn10 = models.CharField(max_length=10, null=True)
    isbn13 = models.CharField(max_length=13, null=True)
    asin = models.CharField(max_length=10, null=True)
    brand = models.CharField(max_length=128, null=True)
    manufacturer = models.CharField(max_length=128, null=True)
    mpn = models.CharField(max_length=64, null=True)
    part_number = models.CharField(max_length=64, null=True)
    sku = models.CharField(max_length=64, null=True)
    model_number = models.CharField(max_length=64, null=True)
    length = models.FloatField(null=True)
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    description = models.CharField(max_length=512, null=True)
    image_url = models.CharField(max_length=512, null=True)
    amazon_url = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def save(self, *args, **kwargs):
        self.onemg = onemg_generator()
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s : %s" % (self.onemg, self.description)

    def generate_barcode(self, type='ean13', text=True):
        barcode_type = BarcodeType.objects.get(name=type.upper())
        try:
            obj = Barcode.objects.get(product=self, type=barcode_type)
        except:
            fp = StringIO()

            if type == 'ean13':
                barcode_text = self.ean
                code_options = dict(includetext=text, textfont='Courier New',
                                           textsize=12, showborder=False)
                margin=1
                scale=1.25
                data_mode=None
            if type == 'upca':
                barcode_text = self.upc
                code_options = dict(includetext=text, textfont='Courier New',
                                           textsize=12, showborder=False)
                margin=1
                scale=1.25
                data_mode = None
            if type == 'qrcode':
                barcode_text = self.amazon_url
                code_options = dict(version=9, eclevel='M')
                margin=10
                scale = 1
                data_mode='8bits'
            
            img = barcode(type, str(barcode_text), options=code_options, margin=margin, scale=scale, data_mode=data_mode)
            
            img.save(fp, format='PNG')
            file = InMemoryUploadedFile(fp, None, "%s-%s.png" % (self.onemg, type),
                                        'image/png', fp.len, None)
            obj = Barcode(product=self, type=barcode_type)
            obj.image.save(file.name, file)
            obj.save()
        return obj



class Barcode(models.Model):
    product = models.ForeignKey(Product)
    type = models.ForeignKey('BarcodeType')
    image = models.FileField(upload_to='barcodes/ean13/', null=True)
    
    class Meta:
        unique_together = ('product', 'type')

    

class BarcodeType(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name



    
