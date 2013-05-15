"""

   news.views

"""


from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


import urllib
from news.models import *

from hp_bs import Parser


def news_login_req(func):
    return login_required(func, login_url='/api-auth/login')
    #return login_required(func, login_url=reverse_lazy('rest_framework.api-auth'))

    
class IndexView(TemplateView):
    template_name = "news_index.html"
    
    @method_decorator(news_login_req)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)
    
def parser(req):
    url = req.POST.get('url', None)
    if url is None:
        return HttpResponse('{}', mimetype="application/json")
    p = Parser(url)
            
    return HttpResponse(p.to_json(), mimetype="application/json")
