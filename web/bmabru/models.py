# -*- coding: utf-8 -*-
"""

"""

import json

from django.contrib.gis.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from bma.api import serializer

@serializer()
class PartnerType(models.Model):
    """
    Define custom partner types
    """
    class Meta:
        verbose_name = _("Partner type")
        verbose_name_plural = _("Partner types")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    parent = models.ForeignKey('PartnerType', verbose_name=_('Parent'), blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
@serializer()
class Partner(models.Model):
    """
    Organisations connected to bMa
    """
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    url = models.URLField(blank=True)
    ptype = models.ForeignKey('PartnerType', verbose_name=_('Partner type'), related_name='partners')
    description = models.TextField(blank=True, verbose_name=_('Description'))
    contact_name = models.CharField(max_length=128, verbose_name=_('Contact name'), blank=True)
    subscribed = models.BooleanField(default=False, verbose_name=_('Subscribed'))
    email = models.EmailField(max_length=128, verbose_name=_('email'), blank=True)
    
    def natural_key(self):
        return (self.id, self.name)
    
    def __unicode__(self):
        return '%s (%s)'%(self.name, self.ptype)
        
@serializer()
class PartnershipType(models.Model):
    """
    Define type of partnership
    """
    class Meta:
        verbose_name = _("Partnership type")
        verbose_name_plural = _("Partnership types")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def __unicode__(self):
        return self.name
        
@serializer()
class Partnership(models.Model):
    """
    Represent how a partner is involved in a project
    """
    class Meta:
        verbose_name = _("Partnership")
        verbose_name_plural = _("Partnerships")
        
    ptype = models.ForeignKey('PartnershipType', verbose_name=_('Partnership type'))
    partner = models.ForeignKey('Partner', verbose_name=_('Partner')) 
    project = models.ForeignKey('Project', verbose_name=_('Project'))
    
@serializer()
class TradeObject(models.Model):
    """
    """
    class Meta:
        verbose_name = _("Trade object")
        verbose_name_plural = _("Trade objects")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
@serializer()
class Program(models.Model):
    """
    building programs
    """
    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name


@serializer()
class Procedure(models.Model):
    """
    Procédure
    """
    class Meta:
        verbose_name = _("Procedure")
        verbose_name_plural = _("Procedures")
    
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
        
class ProjectImage(models.Model):
    """
    An illustration for a project
    """
    class Meta:
        verbose_name = _("Project image")
        verbose_name_plural = _("Project images")
        
    image = models.ImageField(upload_to='project_trigo', height_field='height', width_field='width', verbose_name=_('Image'))
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    zoom_level = models.IntegerField(blank=True)
    

@serializer()
class Function(models.Model):
    """
    Fonction du projet
    """
    class Meta:
        verbose_name = _("Function")
        verbose_name_plural = _("Functions")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name

        
@serializer()
class Mission(models.Model):
    """
    Type de mission
    """
    class Meta:
        verbose_name = _("Mission")
        verbose_name_plural = _("Missions")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
        

        
class ProjectStatus(models.Model):
    """
    Etat d'avancement du projet
    """
    class Meta:
        verbose_name = _("Project status")
        verbose_name_plural = _("Project status")
        
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    order = models.IntegerField()
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
@serializer()
class Action(models.Model):
    """
    ???
    """
    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Actions")
        
    sentence = models.TextField(verbose_name=_('Sentence'))
    project_status = models.ForeignKey('ProjectStatus', verbose_name=_('Project status'))
    
    def natural_key(self):
        return (self.id, self.sentence)
    def __unicode__(self):
        return '%s / %s'%(self.project_status.name, self.sentence[:32])

@serializer()
class Step(models.Model):
    """
    Etapes
    """
    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")
    
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    date = models.DateField(blank=True, null=True, verbose_name=_('Date'))
    
    def __unicode__(self):
        return self.name
     
@serializer()
class City(models.Model):
    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        
    zipcode = models.CharField(max_length=32, verbose_name=_('zip code'))
    name = models.CharField(max_length=256, verbose_name=_('Name'))
    
    def natural_key(self):
        return (self.id, self.zipcode, self.name)
        
    def __unicode__(self):
        return '%s %s'%(self.zipcode, self.name)

@serializer()
class ProjectWorth(models.Model):
    """
    Capital gain?
    """
    class Meta:
        verbose_name = _("Project worth")
        verbose_name_plural = _("Project worth")
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
    
@serializer(property_list = ('centroid', 'geojson'))
class Project(models.Model):
    """
    A project is the main item to present on the website,
    everything else is more or less related to a project
    """
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
    
    published = models.BooleanField(verbose_name=_('Published'),default=False)
    name = models.CharField(verbose_name=_('Name'),max_length=1024)
    description = models.TextField(verbose_name=_('Description'),blank=True)
    address = models.TextField(verbose_name=_('Address'),blank=True)
    surface = models.CommaSeparatedIntegerField(verbose_name=_('Surface'),max_length=64, blank=True)
    budget = models.CommaSeparatedIntegerField(verbose_name=_('Budget'),max_length=64, blank=True)
    trade_name = models.CharField(verbose_name=_('Trade name'),max_length=512, blank=True)
    attribution = models.IntegerField(verbose_name=_('Attribution'),max_length=512, blank=True)
    
    city = models.ForeignKey('City', verbose_name=_('City'),blank=True)
    
    procedure = models.ForeignKey('Procedure', verbose_name=_('Procedure'),blank=True)
    mission = models.ForeignKey('Mission', verbose_name=_('Mission'),blank=True)
    trade_object = models.ForeignKey('TradeObject', verbose_name=_('Trade object'),blank=True) 
    
    programs = models.ManyToManyField('Program', verbose_name=_('Programs'),blank=True)
    image = models.ManyToManyField('ProjectImage', verbose_name=_('Project Images'),blank=True)
    functions = models.ManyToManyField('Function', verbose_name=_('Functions'),blank=True)
    steps = models.ManyToManyField('Step', blank=True)
    actions = models.ManyToManyField('Action', verbose_name=_('Actions'),blank=True)
    worth = models.ManyToManyField('ProjectWorth', verbose_name=_('Project worths'),blank=True)
    
    
    mpoly = models.MultiPolygonField(verbose_name=_('Perimeter'), srid=4326, geography=True)
    objects = models.GeoManager()
    
    parent = models.ForeignKey( 'Project', verbose_name=_('Parent'), blank=True)
    
    slug = models.SlugField(max_length=255, editable=False, default='None')
    
    def get_city_display(self):
        return '%s %s'%(self.city.zipcode, self.city.name)
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(force_insert, force_update) 
    
    @property
    def centroid(self):
        try:
            return json.loads(self.mpoly.centroid.geojson)
        except:
            return  { "type": "Point", "coordinates": [ 0, 0 ] }
        
    @property
    def geojson(self):
        return json.loads(self.mpoly.geojson)
    
        
    def __unicode__(self):
        return self.name







