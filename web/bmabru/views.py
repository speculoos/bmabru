# -*- coding: utf-8 -*-
"""
bmabru.views
"""


from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from bmabru.models import (Project, ProjectImage, Builder)


def index(request):
    return render_to_response("base.html", {}, context_instance = RequestContext(request))
