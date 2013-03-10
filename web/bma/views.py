# bma.views

import json

from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.exceptions import PermissionDenied

from bma import settings

WHITE_LIST = (
    'LANGUAGES',
    'MEDIA_URL',
    'STATIC_URL',
    'DEBUG',
    'TIME_ZONE',
    )

def config(req, q):
    if q not in WHITE_LIST:
        raise PermissionDenied
    try:
        data = json.dumps({q:getattr(settings,q)})
    except Exception as e:
        raise Http404('%s'%e)
    return HttpResponse(data, mimetype="application/json")
    