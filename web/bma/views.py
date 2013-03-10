# bma.views

import json

from django.http import HttpResponse, Http404
from django.template import RequestContext

from bma import settings


def config(req, q):
    try:
        data = json.dumps({q:settings[q]})
    except Exception:
        raise Http404()
    return HttpResponse(data, mimetype="application/json")