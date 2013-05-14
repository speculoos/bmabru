"""
    helpers for django-rest-framework
"""

import  django.db.models
            
from rest_framework import serializers
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated

from django.conf.urls import  url


REGISTERED_MODELS = []

@api_view(('GET',))
@permission_classes((IsAuthenticated, ))
def api_root(request, format=None):
    r = {}
    for M in REGISTERED_MODELS:
        r[M+'s'] = reverse('%s-list'%(M,), request=request, format=format)
    return Response(r)

# class decorator
def serializer(property_list = tuple(), exclude=tuple()):
    def decorator(cls):
        name = cls.__name__
        #print('Decorating [%s] with a serializer'%(name,))
        meta = type('Meta', (object, ), {'model':cls, 'depth':3, 'exclude':exclude})
        srl = type(''.join([name,'Serializer']), (serializers.ModelSerializer,), {'Meta':meta} )

        fields = {}
        for prop in property_list:
            is_fk = issubclass(type(getattr(cls, prop)), 
                            django.db.models.related.ForeignRelatedObjectsDescriptor)
                            
            if is_fk:
                sfield = getattr(cls, prop).related.model.serializer_class(many=True)
            else:
                sfield = serializers.Field(source=prop)
                
            setattr(srl, prop, sfield)
            fields[prop] = sfield
        if property_list:
            setattr(srl, 'base_fields', fields)
            
        setattr(cls, 'serializer_class', srl)
        return cls
    return decorator

def get_queryset(self):
        qs = self.model.objects.all()
        if self._filters != None:
            for f in self._filters:
                qs = qs.filter(**f)
        return qs

def get_list_view(app, model, filters=None):
    mi = __import__('.'.join([app,'models']), globals(), locals(), [model], 0)
    m = getattr(mi, model)
    cls = type(''.join([app,model,'List']), (generics.ListCreateAPIView,), {})
    setattr(cls, '_filters', filters)
    setattr(cls, 'model', m)
    setattr(cls, 'serializer_class', m.serializer_class)
    setattr(cls, 'get_queryset', get_queryset)
    
    return cls
    
def get_detail_view(app, model):
    mi = __import__('.'.join([app,'models']), globals(), locals(), [model], 0)
    m = getattr(mi, model)
    cls = type(''.join([app,model,'Detail']), (generics.RetrieveUpdateDestroyAPIView,), {})
    setattr(cls, 'model', m)
    setattr(cls, 'serializer_class', m.serializer_class)
    
    return cls
    

#@api_view(['GET','POST'])


def view_list(request, app, model, filters):
    view_cls = get_list_view(app, model, filters)
    #return view(request)
    v = view_cls.as_view()
    return v(request)
    
#@api_view(['GET','POST', 'PUT'])


def view_detail(request, app, model, pk):
    view_cls = get_detail_view(app, model)
    #return view(request, pk=pk)
    return view_cls.as_view()(request, pk=pk)
    
def urls(resources):
    """
        resources is an iterable containing tuples of the form:
        (app_name, model_name, filters )
    """
    ret = []
    for r in resources:
        app = r[0]
        m = r[1]
        f = r[2]
        mn = m.lower() 
        ret.append(url(
            r''.join(['^api/', mn + 's' ,'/$']),
            'bma.api.view_list',
            {'app': app, 'model':m, 'filters':f},
            name= mn + '-list'
            ),
        )
        ret.append(url(
            r''.join(['^api/', mn + 's' ,'/(?P<pk>\d+)$']),
            'bma.api.view_detail',
            {'app': app, 'model':m},
            name= mn + '-detail'
            )
        )
        REGISTERED_MODELS.append(mn)
        
    return tuple(ret)