from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

import urllib, cStringIO
import re

from products import amazon_utils
from products.forms import ProductForm


def home(request):
    if request.method == 'POST':
        productform = ProductForm(request.POST)
        if productform.is_valid():
            code = productform.cleaned_data['ASIN']
            asin = re.compile("^B\d{2}\w{7}|\d{9}(X|\d)$")
            if asin.match(code):
                product = amazon_utils.get_or_create_product(code)
                ean = product.generate_barcode(type='ean13')
                upc = product.generate_barcode(type='upca')
                qrcode = product.generate_barcode(type='qrcode', text=False)
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
                              },
                              context_instance = RequestContext(request))
    
