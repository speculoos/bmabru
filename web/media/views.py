# media.views

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.utils import six
import json
from markdown2 import markdown

from media.models import *

class MarkdownSerial(serializers.get_serializer("json")):
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
        mdvalue = markdown(value)
        self._current[prop] = mdvalue

def media_json(request, mid):
    try:
        media = Page.objects.filter(pk=mid)
    except Exception:
        raise Http404()
        
    js = MarkdownSerial()
    data = js.serialize(media, indent=2, use_natural_keys=True, props=['body']);
    return HttpResponse(data, mimetype="application/json")

    
def page(request, page_slug):
    data = {'category':Category.objects.all()}
    try:
        p = Page.objects.filter(slug=page_slug)
        data['current_page'] = p[0]
    except Exception as e:
        raise Http404('Page "%s" Not Found'%(page_slug))
    return render_to_response("page.html", data, context_instance = RequestContext(request))