# -*- coding: utf-8 -*-
import sys
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bma.settings")
    
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'../web')))

from django.db.models.loading import get_models
_models = get_models()

import re
from bmabru.models import *
from django.db import connection
from django.utils.translation import get_language

from shapely.geometry import shape, MultiPolygon

import fiona


print 'Using language: {}'.format(get_language())

def append_shape(shapes, f):
    props = f['properties']
    name = props['name'].lower()
    shapes[name] = f

shapes = {}

with fiona.open(sys.argv[1], 'r') as source:
    
    for f in source:
        try:
            append_shape(shapes, f)
        
        except Exception, e:
            # Writing uncleanable features to a different shapefile
            # is another option.
            print("Error appending feature %s: %s"%(f['id'], e))
            
cities = City.objects.all()

for city in cities:
    nm = '-'.join([city.name_fr,city.name_nl]).lower()
    parts = nm.split('-')
    matches = []
    for n in parts:
        if n:
            rx = re.compile(n)
            for k in shapes:
                if rx.match(k) and k not in matches:
                    matches.append(k)
    if len(matches) == 0:
        continue
    print u'Pick a choice for: {} | {}'.format(city.name_fr,city.name_nl)
    c = 0
    for m in matches:
        print u'{}: {}'.format(c, m)
        c += 1
    s = input('> ')
    si = int(s)
    key = matches[si]
    print u'Selected: {} {}'.format(key, shapes[key]['id'])
    simport = shape(shapes[key]['geometry'])
    if simport.geom_type == 'Polygon':
        simport = [simport]
        
    mpoly = MultiPolygon(simport)
    city.geom = mpoly.wkt
    city.save()
