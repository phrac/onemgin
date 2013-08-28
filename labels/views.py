from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from products import amazon_utils
from products.forms import ProductForm


def home(request):
    if request.method == 'POST':
        productform = ProductForm(request.POST)
        if productform.is_valid():
            product = amazon_utils.get_or_create_product(productform.cleaned_data['code'])
            barcode = product.generate_barcode()
            response = HttpResponse(content_type='image/png')
            response.write(barcode.getvalue())
            return response
    
    else:
        productform = ProductForm()
    return render_to_response('labels/home.html',
                              {
                                  'product_form': productform,
                              },
                              context_instance = RequestContext(request))
    
