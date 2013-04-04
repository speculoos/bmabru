"""
    helpers for django-rest-framework
"""

from rest_framework import serializers
from rest_framework import generics
from rest_framework.decorators import api_view

from django.conf.urls import  url



# class decorator
def serializer(property_list = tuple()):
    def decorator(cls):
        name = cls.__name__
        #print('Decorating [%s] with a serializer'%(name,))
        meta = type('Meta', (object, ), {'model':cls, 'depth':9})
        srl = type(''.join([name,'Serializer']), (serializers.ModelSerializer,), {'Meta':meta} )

        fields = {}
        for prop in property_list:
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
    cls = type(''.join([app,model,'List']), (generics.ListAPIView,), {})
    setattr(cls, '_filters', filters)
    setattr(cls, 'model', m)
    setattr(cls, 'serializer_class', m.serializer_class)
    setattr(cls, 'get_queryset', get_queryset)
    
    return cls().as_view()
    
def get_detail_view(app, model):
    mi = __import__('.'.join([app,'models']), globals(), locals(), [model], 0)
    m = getattr(mi, model)
    cls = type(''.join([app,model,'Detail']), (generics.RetrieveAPIView,), {})
    setattr(cls, 'model', m)
    setattr(cls, 'serializer_class', m.serializer_class)
    
    return cls().as_view()
    

@api_view(['GET'])
def view_list(request, app, model, filters):
    view = get_list_view(app, model, filters)
    return view(request)
    
@api_view(['GET'])
def view_detail(request, app, model, pk):
    view = get_detail_view(app, model)
    return view(request, pk=pk)
    
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
        
        
    return tuple(ret)