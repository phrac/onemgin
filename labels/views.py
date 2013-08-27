from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext


def home(request):

    return render_to_response('labels/home.html',
                              {
                              },
                              context_instance = RequestContext(request))
    
