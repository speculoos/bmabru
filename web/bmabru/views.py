# -*- coding: utf-8 -*-
"""
bmabru.views
"""


from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.utils import six
import json

from bmabru.models import *
from media.models import *


class GeoSerial(serializers.get_serializer("json")):
    def serialize(self, queryset, **options):
        """
        Serialize a queryset.
        """
        self.options = options

        self.stream = options.pop("stream", six.StringIO())
        self.selected_fields = options.pop("fields", None)
        self.use_natural_keys = options.pop("use_natural_keys", False)
        self.property_list = options.pop('props', [])

        self.start_serialization()
        self.first = True
        for obj in queryset:
            self.start_object(obj)
            # Use the concrete parent class' _meta instead of the object's _meta
            # This is to avoid local_fields problems for proxy models. Refs #17717.
            concrete_model = obj._meta.concrete_model
            for field in concrete_model._meta.local_fields:
                if field.serialize:
                    if field.rel is None:
                        if self.selected_fields is None or field.attname in self.selected_fields:
                            self.handle_field(obj, field)
                    else:
                        if self.selected_fields is None or field.attname[:-3] in self.selected_fields:
                            self.handle_fk_field(obj, field)
            for field in concrete_model._meta.many_to_many:
                if field.serialize:
                    if self.selected_fields is None or field.attname in self.selected_fields:
                        self.handle_m2m_field(obj, field)
            for prop in self.property_list:
                self.handle_property(obj, prop)
                
            self.end_object(obj)
            if self.first:
                self.first = False
        self.end_serialization()
        return self.getvalue()
        
    def handle_property(self, obj, prop):
        value = getattr(obj,prop)
        self._current[prop] = json.loads(value)


def index(request):
    data = {'category':Category.objects.all()}
    return render_to_response("index.html", data, context_instance = RequestContext(request))
    
def projects(request):
    prjcts = Project.objects.filter(published=True)
    cats = Category.objects.all()
    return render_to_response("projects.html", {'category':cats, 'projects':prjcts}, context_instance = RequestContext(request))

def project(request, project):
    data = {'category':Category.objects.all()}
    try:
        p = Project.objects.filter(slug=project)
        data['current_project'] = p[0]
    except Exception as e:
        raise Http404('Project "%s" Not Found'%(project))
    return render_to_response("project.html", data, context_instance = RequestContext(request))
    
def projects_json(request):
    #jr = serializers.get_serializer("json")()
    jr = GeoSerial()
    data = jr.serialize(Project.objects.filter(published=True), indent=2, use_natural_keys=True, props=['centroid','geojson'])
    return HttpResponse(data, mimetype="application/json")
