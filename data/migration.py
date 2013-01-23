# -*- coding: utf-8 -*-
"""
Data migration script
From previous Officity based web site to Django based one

"""
import os
import sys

import HTMLParser
_html_parser = HTMLParser.HTMLParser()
_ts = type('')
_tu = type(u'')
def ue(s):
    if type(s) == _ts or type(s) == _tu:
        return _html_parser.unescape(s)
    return u''

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bma.settings")


for d in sys.argv[1:]:
    path =  d
    if path not in sys.path:
        sys.path.append(path)


import json
from bmabru.models import *

fj = open('projects.json')
pdata = json.load(fj)


builders = {}
cities = {}
missions = {}
fonctions = {}
procedures = {}
for p in pdata:
    for b in p['builder']:
        builders[b['ID']] = b
        
    cities[p['ZIP']['value']] = p['ZIP']  

    for m in p['mission']:
        missions[m['value']] = m
        
    for f in p['fonctions']:
        fonctions[f['value']] = f
        
    procedures[p['CONTRACTTYPE']['value']] = p['CONTRACTTYPE']
    
## import buiders
try:
    partner_type = PartnerType.objects.get(name=u'Maître d’ouvrage')
except Exception:
    partner_type = PartnerType.objects.create(name_fr = u'Maître d’ouvrage', name_nl = u'Bouwheren')
    partner_type.save()

for b in builders:
    print 'Import Builder %s'%(b,)
    nb = Partner.objects.create(name_fr=ue(builders[b]['fre']), name_nl = ue(builders[b]['dut']), ptype=partner_type)
    builders[b]['django_id'] = nb.save()
    
    
## import cities
for c in cities:
    print 'Import City %s'%(c,)
    city = cities[c]
    zc = int(c)
    nfr = ' '.join(city['fre'].split(' ')[1:])
    nnl = ' '.join(city['dut'].split(' ')[1:])
    co = City.objects.create(zipcode=zc, name_fr=nfr, name_nl=nnl)
    cities[c]['django_id'] = co.save()

## import missions
for m in missions:
    print 'Import Mission %s'%(m,)
    mis = missions[m]
    nm = Mission.objects.create(name_fr=ue(mis['fre']), name_nl=ue(mis['dut']))
    missions[m]['django_id'] = nm.save()
    
## import fonctions
for f in fonctions:
    print 'Import Fonction %s'%(f,)
    fonc = fonctions[f]
    nf = Function.objects.create(name_fr=ue(fonc['fre']), name_nl=ue(fonc['dut']))
    fonctions[f]['django_id'] = nf.save()

## import procedures
for p in procedures:
    print 'Import Procedure %s'%(p,)
    proc = procedures[p]
    np = Procedure.objects.create(name_fr=ue(proc['fre']), name_nl=ue(proc['dut']))
    procedures[p]['django_id'] = np.save()