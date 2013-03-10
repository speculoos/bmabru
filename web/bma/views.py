# bma.views

import json

from django.http import HttpResponse, Http404
from django.template import RequestContext

from bma import settings


def config(req, q):
    try:
        data = json.dumps({q:getattr(settings,q)})
    except Exception as e:
        raise Http404('%s'%e)
    return HttpResponse(data, mimetype="application/json")