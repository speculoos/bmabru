# -*- coding: utf-8 -*-
"""
bmabru.views
"""


from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.utils import six
from django.core.urlresolvers import reverse
import json

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from bmabru.models import *
from media.models import *

from bma.api import get_list_view



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
    data['featured'] = Featured.objects.filter(published=True)
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
    
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'projects': reverse('project-list', request=request),
    })
    
@api_view(['GET'])
def api_view_list(request, model, filters):
    view = get_list_view('bmabru', model, filters)
    return view(request)
    
    
def expose_structure(req):
    from bmabru.admin import GeoAdmin
    pm = Project()._meta
    
    def unfold_rel(mdl, msg):
        objs = mdl.objects.all()
        msg.append(' '.join([' <a style="font-family:sans-serif;font-size:120%;color:#999;" href="',
                reverse('admin:bmabru_'+model._meta.module_name+'_add'),
                '" target="_blank">Ajouter</a>']))
        msg.append('<ul style="list-style-type:none">')
        for o in objs:
            msg.append(' '.join([
                '<li>',
                '<span style="font-family:sans-serif;font-size:70%;color:#999;font-weight:bold">',
                str(o.id),
                '</span> ',
                o.__unicode__(),
                ' <a style="font-family:sans-serif;font-size:90%;color:#999;" href="',
                reverse('admin:bmabru_'+model._meta.module_name+'_change', args=(o.id,)),
                '" target="_blank">modifier</a>',
                '</li>'
            ]))
        msg.append('</ul>')
        
    
    html = []
    tstr = type('')
    for block in GeoAdmin.fieldsets:
        fields = block[1]['fields']
        for line in fields:
            tline = line
            if type(line) == tstr:
                tline = (line,)
            for field in tline:
                f = pm.get_field(field)
                if f.rel:
                    html.append(''.join(['<h2>', unicode(f.verbose_name), '</h2>' ]))
                    model = f.rel.to
                    unfold_rel(model, html)
                else:
                    html.append(''.join(['<h3>', unicode(f.verbose_name), '</h3>' ]))
                    
                for inline in GeoAdmin.inlines:
                    if inline.after_field == field:
                        html.append(''.join(['<h2>', unicode(inline.model._meta.verbose_name_plural), '</h2>' ]))
                        unfold_rel(inline.model, html)
                    
    return HttpResponse('\n'.join(html))
    
