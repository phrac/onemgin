from django.db import models


def onemg_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

class Product(models.Model):
    onemg = models.CharField(max_length=13, unique=True)
    ean = models.IntegerField(max_length=13, unique=True)
    upc = models.IntegerField(max_length=12, unique=True)
    jan = models.CharField(max_length=13)
    gtin = models.CharField(max_length=14)
    nsn = models.CharField(max_length=14)
    isbn10 = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    asin = models.CharField(max_length=10)
    description = models.CharField(max_length=512)

    def save(self, *args, **kwargs):
        self.onemg = onemg_generator()
        try:
            super(Product, self).save(*args, **kwargs)
        except:
            self.save()


    
