from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

import urllib, cStringIO
import re

from products import amazon_utils
from products.models import Product
from products.forms import ProductForm


def home(request):
    recents = Product.objects.filter(image_url__isnull=False).order_by('-created')[:6]
    if request.method == 'POST':
        productform = ProductForm(request.POST)
        if productform.is_valid():
            print 'valid'
            code = productform.cleaned_data['ASIN']
            asin = re.compile("^B\d{2}\w{7}|\d{9}(X|\d)$")
            print 're compiled'
            if asin.match(code):
                product = amazon_utils.get_or_create_product(code)
            else:
                print 'no match'
                asin = amazon_utils.random_product()

                product = amazon_utils.get_or_create_product(asin)
                print 'generated product'
            ean = product.generate_barcode(type='ean13')
            print 'generated ean'
            upc = product.generate_barcode(type='upca')
            print 'generaged upca'
            qrcode = product.generate_barcode(type='qrcode', text=False)
            print 'generated qr'
            return render_to_response('labels/generator_output.html', 
                                    {
                                     'product': product,
                                     'ean': ean,
                                     'upc': upc,
                                     'qrcode': qrcode,
                                     
                                    },
                                    context_instance=RequestContext(request))
    
    else:
        productform = ProductForm()
    return render_to_response('labels/home.html',
                              {
                                  'product_form': productform,
                                  'recents': recents,
                              },
                              context_instance = RequestContext(request))
    
