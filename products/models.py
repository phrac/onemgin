from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    description = models.CharField(max_length=512, null=True)
    image_url = models.CharField(max_length=512, null=True)
    amazon_url = models.URLField(null=True)


    def save(self, *args, **kwargs):
        self.onemg = onemg_generator()
        super(Product, self).save(*args, **kwargs)

    def generate_barcode(self, type='ean13', text=True):
        fp = StringIO()

        from elaphe import barcode
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
        
        barcode = barcode(type, str(barcode_text), options=code_options, margin=margin, scale=scale, data_mode=data_mode)
        
        barcode.save(fp, format='PNG')
        file = InMemoryUploadedFile(fp, None, "%s-%s.png" % (self.onemg, type),
                                    'image/png', fp.len, None)
        barcode_type = BarcodeType.objects.get(name=type.upper())
        try:
            obj = Barcode.objects.get(product=self, type=barcode_type)
        except:
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



    
