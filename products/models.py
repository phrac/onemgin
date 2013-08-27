from django.db import models
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
    barcodes = models.ManyToManyField("Barcode",
                                      related_name="product_barcodes")

    def save(self, *args, **kwargs):
        self.onemg = onemg_generator()
        super(Product, self).save(*args, **kwargs)

    def generate_barcode(self, type='EAN'):
        import barcode
        from StringIO import StringIO
        fp = StringIO()
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(self.ean)
        ean.write(fp)
        return fp



class Barcode(models.Model):
    type = models.ForeignKey('BarcodeType')
    image = models.FileField(upload_to=barcode_file_name, null=True)

class BarcodeType(models.Model):
    name = models.CharField(max_length=32)



    
