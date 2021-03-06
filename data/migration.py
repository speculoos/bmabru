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
from django.db import connection

fj = open('projects.json')
pdata = json.load(fj)

fg = open('geom.json')
gdata = json.load(fg)

def geom(pid):
    for g in gdata:
        if g['pid'] == pid:
            return g['geom']
    return 'MULTIPOLYGON EMPTY'
    #raise Exception('No geom for %d'%pid)



builders = {}
cities = {}
missions = {}
fonctions = {}
procedures = {}
budget_ranges = {}
surface_ranges = {}
status = {
'PROJECT_STEP_1_PROGRAM':{},
'PROJECT_STEP_2_CSC':{},
'PROJECT_STEP_3_ADVICE':{},
'PROJECT_STEP_4_QUALITY':{},
'PROJECT_STEP_5_JURY':{},
'PROJECT_STEP_6_ATTRIBUTION':{},
'PROJECT_STEP_7_DEV':{}
}

for s in status:
    sa = s.split('_')
    order = int(sa[2]) * 1
    name = sa[-1].capitalize()
    status[s]['order'] = order
    status[s]['name'] = name
    o = ProjectStatus.objects.create(name=name, order=order)
    status[s]['object'] = o
    o.save()
    status[s]['django_id'] = o.pk
    status[s]['actions'] = {}
    print 'Imported Status %s as %d'%(status[s]['name'], status[s]['django_id'])

for p in pdata:
    for b in p['builder']:
        builders[b['ID']] = b
    if p['ZIP']['value'] != '':
        cities[p['ZIP']['value']] = p['ZIP']

    for m in p['mission']:
        missions[m['value']] = m
        
    for f in p['fonctions']:
        fonctions[f['value']] = f
        
    
    if p['CONTRACTTYPE']['value'] == '':
        procedures['undefined'] = {'dut':'undefined', 'fre': 'undefined', 'value':'undefined'}
    else:
        procedures[p['CONTRACTTYPE']['value']] = p['CONTRACTTYPE']
    
    for s in status:
        ps = p[s]
        status[s]['actions'][ps['value']] = ps
        
    try:
        surface_ranges[p['SURFACE']] = None
    except Exception:
        pass
    
## DEFAULTS
default_city = City.objects.create(zipcode=9999, name_fr=u'None City', name_nl=u'None City')
default_city.save()

default_mission = Mission.objects.create(name_fr=u'No Mission', name_nl=u'No Mission')
default_mission.save()

ptype_mo = PartnershipType.objects.create(name_fr=u'Maitrise d’ouvrage', name_nl=u'Bouwheer')
ptype_mo.save()

acteur_decision = PartnerType.objects.create(name_fr=u'Acteur décision', name_nl=u'-')
acteur_decision.save()
mo_reg_adm = PartnerType.objects.create(name_fr=u'MO. Régional Administration', name_nl=u'-', parent=acteur_decision)
mo_reg_adm.save()

    
## import buiders
#try:
    #partner_type = PartnerType.objects.get(name=u'Maître d’ouvrage')
#except Exception:
    #partner_type = PartnerType.objects.create(name_fr = u'Maître d’ouvrage', name_nl = u'Bouwheren')
    #partner_type.save()

for b in builders:
    print 'Import Builder %s'%(b,)
    nb = Partner.objects.create(name_fr=ue(builders[b]['fre']), name_nl = ue(builders[b]['dut']), ptype=mo_reg_adm)
    nb.save()
    builders[b]['django_id'] = nb
    
    
## import cities
for c in cities:
    print 'Import City %s'%(c,)
    try:
        city = cities[c]
        zc = int(c)
        nfr = ' '.join(city['fre'].split(' ')[1:])
        nnl = ' '.join(city['dut'].split(' ')[1:])
        co = City.objects.create(zipcode=zc, name_fr=nfr, name_nl=nnl)
        co.save()
        cities[c]['django_id'] = co
    except Exception:
        print 'FAILED to import city %s'%(c,)

## import missions
for m in missions:
    print 'Import Mission %s'%(m,)
    mis = missions[m]
    nm = Mission.objects.create(name_fr=ue(mis['fre']), name_nl=ue(mis['dut']))
    nm.save()
    missions[m]['django_id'] = nm
    
## import fonctions
for f in fonctions:
    print 'Import Fonction %s'%(f,)
    fonc = fonctions[f]
    nf = Function.objects.create(name_fr=ue(fonc['fre']), name_nl=ue(fonc['dut']))
    nf.save()
    fonctions[f]['django_id'] = nf

## import procedures
for p in procedures:
    print 'Import Procedure %s'%(p,)
    try:
        proc = procedures[p]
    except Exception:
        proc = procedures['undefined']
    np = Procedure.objects.create(name_fr=ue(proc['fre']), name_nl=ue(proc['dut']))
    np.save()
    procedures[p]['django_id'] = np
    
## import actions
for s in status:
    ss = status[s]
    for a in ss['actions']:
        print 'Import Action %s'%(a,)
        act = ss['actions'][a]
        na = Action.objects.create(sentence_fr=ue(act['fre']), sentence_nl=ue(act['dut']), project_status=ss['object'])
        na.save()
        ss['actions'][a]['django_id'] = na
        
## import surfaces
for sr in surface_ranges:
    print 'Import Surface %s'%(sr,)
    try:
        f, c = list(sr.split('-'))
        ff = f.split('m')[0]
        cc = c.split('m')[0]
        fff = int(''.join(ff.split('.')))
        ccc = int(''.join(cc.split('.')))
        surf = SurfaceRange.objects.create(floor=fff, ceiling=ccc)
        surf.save()
        surface_ranges[sr] = surf
    except Exception:
        print 'Failed to import surface [%s]'%sr
    
    
        
## import projects

for p in pdata:
    
    #new_p = Project.objects.create()
    new_p = Project()
    
    new_p.published = p['PUBLISHED'] == '1'
    new_p.name_fr = ue(p['TITLE']['fre'])
    new_p.name_nl = ue(p['TITLE']['dut'])
    new_p.attribution = 0
    try:
        new_p.description_fr = ue(p['BODY']['fre'])
        new_p.description_nl = ue(p['BODY']['dut'])
    except Exception:
        print 'No description for %s %s'%(p['ID'], ue(p['TITLE']['fre']))
        
    
    try:
        address = p['ADDRESS']
        try:
            new_p.address_fr = ue(address['fre']) 
        except Exception:
            print 'No FRE address for %s %s'%(p['ID'], ue(p['TITLE']['fre']))
        try:
            new_p.address_nl = ue(address['dut'])
        except Exception:
            print 'No DUT address for %s %s'%(p['ID'], ue(p['TITLE']['fre']))
            
    except Exception:
        print 'No address for %s %s'%(p['ID'], ue(p['TITLE']['fre']))
        
    
    try:
        new_p.city = cities[p['ZIP']['value']]['django_id']
    except Exception:
        new_p.city = default_city
        pass

    if p['CONTRACTTYPE']['value'] == '':
        new_p.procedure = procedures['undefined']['django_id']
    else:
        new_p.procedure = procedures[p['CONTRACTTYPE']['value']]['django_id']
        
    if  p['mission']:
        for m in p['mission']:
            new_p.mission = missions[m['value']]['django_id']
    else:
        new_p.mission = default_mission
        
    new_p.mpoly = geom(int(p['ID']))
    
    try:
        new_p.save()
    except Exception as e:
        print 'Failed to register %s %s => %s'%(p['ID'], ue(p['TITLE']['fre']), e)
        connection._rollback()
        continue
        
    
    try:
        new_p.surface_range = surface_ranges[p['SURFACE']]
    except Exception:
        print 'Failed to set surface'
    
        
    for f in p['fonctions']:
        new_p.functions.add(fonctions[f['value']]['django_id'])
    
    for s in status:
        ps = p[s]
        new_p.actions.add(status[s]['actions'][ps['value']]['django_id'])
        
    new_p.save()
    
    
    for b in p['builder']:
        # create a new partnership
        pship = Partnership.objects.create(ptype=ptype_mo, partner=builders[b['ID']]['django_id'], project=new_p)
        pship.save()
    
    
