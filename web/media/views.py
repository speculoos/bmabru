# media.views

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers

from media.models import *
#import json


def media_json(request, mid):
    try:
        media = Page.objects.filter(pk=mid)
    except Exception:
        raise Http404()
        
    js = serializers.get_serializer("json")()
    data = js.serialize(media, indent=2, use_natural_keys=True);
    return HttpResponse(data, mimetype="application/json")
