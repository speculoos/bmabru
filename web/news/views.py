"""

   news.views

"""


from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

import urllib
from news.models import *

from hp_bs import Parser


def render_body(req, id):
    n = News.object.get(pk=id)
    
    
class IndexView(TemplateView):
    template_name = "news_index.html"
    
def parser(req):
    url = req.POST.get('url', None)
    if url is None:
        return HttpResponse('{}', mimetype="application/json")
    p = Parser(url)
            
    return HttpResponse(p.to_json(), mimetype="application/json")
