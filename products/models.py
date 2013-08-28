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
        #from reportlab.lib.units import mm
        #from reportlab.graphics.barcode import createBarcodeDrawing
        #from reportlab.graphics.shapes import Drawing, String
        #from reportlab.graphics.charts.barcharts import HorizontalBarChart
        #barcode = createBarcodeDrawing('EAN13', value=str(self.upc),
        #                               width=144, height=72, ratio=5.75, humanReadable=True)

        from django.core.files.uploadedfile import InMemoryUploadedFile
        from StringIO import StringIO
        #import barcode
        fp = StringIO()
        #EAN = barcode.get_barcode_class('ean13')
        #ean = EAN(str(self.ean))
        #ean.write(fp)
        #generate('EAN13', str(self.ean), writer=ImageWriter(), output=fp)
        from elaphe import barcode
        barcode = barcode('ean13', str(self.ean),
                          options=dict(includetext=True, textfont='Courier New',
                                       textsize=12, showborder=False),
                          margin=1, scale=1.25)
        
        barcode.save(fp, format='PNG')
        file = InMemoryUploadedFile(fp, None, "%s-EAN13.png" % self.onemg,
                                    'image/png', fp.len, None)
        barcode_type = BarcodeType.objects.get(name='EAN13')
        obj = Barcode(type=barcode_type)
        obj.image.save(file.name, file)
        return obj



class Barcode(models.Model):
    type = models.ForeignKey('BarcodeType')
    image = models.FileField(upload_to='barcodes/ean13/', null=True)

class BarcodeType(models.Model):
    name = models.CharField(max_length=32)



    
