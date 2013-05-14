"""

   news.views

"""
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

import urllib
from news.models import *

from hp_bs import Parser


def render_body(req, id):
    n = News.object.get(pk=id)
    
    
def index(req):
    pass
    
    
    
def parser(req):
    url = req.GET.get('url', None)
    if url is None:
        return HttpResponse('{}', mimetype="application/json")
    p = Parser(url)
            
    return HttpResponse(p.to_json(), mimetype="application/json")
