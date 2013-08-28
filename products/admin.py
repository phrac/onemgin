from django.contrib import admin
from products.models import Product, Barcode, BarcodeType

admin.site.register(Product)
admin.site.register(Barcode)
admin.site.register(BarcodeType)
