# -*- coding: utf-8 -*-
"""

"""

import json

from django.contrib.gis.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import localize

from bma.api import serializer
from easy_thumbnails.files import get_thumbnailer

@serializer()
class PartnerType(models.Model):
    """
    Define custom partner types
    """
    class Meta:
        verbose_name = _("Partner type")
        verbose_name_plural = _("Partner types")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    parent = models.ForeignKey('PartnerType', verbose_name=_('Parent'), blank=True, null=True)
    
    def __unicode__(self):
        if self.parent:
            return u'%s > %s'%(self.parent.__unicode__(), self.name, )
        return self.name
    
@serializer(exclude=('ptype','description','contact_name','subscribed','email'))
class Partner(models.Model):
    """
    Organisations connected to bMa
    """
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")
        ordering = ['name']
        
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
        
@serializer(exclude=('description',))
class PartnershipType(models.Model):
    """
    Define type of partnership
    """
    class Meta:
        verbose_name = _("Partnership type")
        verbose_name_plural = _("Partnership types")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def __unicode__(self):
        return self.name
        
@serializer(property_list=('ptype','partner',),exclude=('project',))
class Partnership(models.Model):
    """
    Represent how a partner is involved in a project
    """
    class Meta:
        verbose_name = _("Partnership")
        verbose_name_plural = _("Partnerships")
        
    ptype = models.ForeignKey('PartnershipType', verbose_name=_('Partnership type'))
    partner = models.ForeignKey('Partner', verbose_name=_('Partner')) 
    project = models.ForeignKey('Project', verbose_name=_('Project'), related_name="partnerships")
    
    def __unicode__(self):
        return u'%s: %s'%(self.ptype, self.partner)
    
@serializer(exclude=('description',))
class TradeObject(models.Model):
    """
    """
    class Meta:
        verbose_name = _("Trade object")
        verbose_name_plural = _("Trade objects")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
@serializer(exclude=('description',))
class Program(models.Model):
    """
    building programs
    """
    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name


@serializer(exclude=('description',))
class Procedure(models.Model):
    """
    Procédure
    """
    class Meta:
        verbose_name = _("Procedure")
        verbose_name_plural = _("Procedures")
        ordering = ['name']
    
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
@serializer(property_list=('thumbnail','url', 'large'))
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
    zoom_level = models.IntegerField(blank=True, default=1)
    notice = models.TextField(blank=True, verbose_name=_('Notice'))
    
    @property
    def thumbnail(self):
        from easy_thumbnails.files import get_thumbnailer
        options = {'size': (360 /2, 240 /2), 'crop': True}
        return get_thumbnailer(self.image).get_thumbnail(options).url
        
    @property
    def large(self):
        from easy_thumbnails.files import get_thumbnailer
        options = {'size': (360 *2.5, 240 *2.5), 'crop': 'smart', 'upscale': True}
        return get_thumbnailer(self.image).get_thumbnail(options).url
        
    @property
    def url(self):
        return self.image.url
    
    def __unicode__(self):
        return ('%s' % (self.image, )).split('/').pop()
    

@serializer(exclude=('description',))
class Function(models.Model):
    """
    Fonction du projet
    """
    class Meta:
        verbose_name = _("Function")
        verbose_name_plural = _("Functions")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name

        
@serializer(exclude=('description',))
class Mission(models.Model):
    """
    Type de mission
    """
    class Meta:
        verbose_name = _("Mission")
        verbose_name_plural = _("Missions")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
        

        
@serializer()
class ProjectStatus(models.Model):
    """
    Etat d'avancement du projet
    """
    class Meta:
        verbose_name = _("Project status")
        verbose_name_plural = _("Project status")
        ordering = ['order']
        
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    order = models.IntegerField()
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
@serializer(property_list=('project_status',))
class Action(models.Model):
    """
    ???
    """
    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Actions")
        ordering = ['project_status__order', 'sentence']
        
    sentence = models.TextField(verbose_name=_('Sentence'))
    project_status = models.ForeignKey('ProjectStatus', verbose_name=_('Project status'))
    
    
    def natural_key(self):
        return (self.id, self.sentence)
    def __unicode__(self):
        return '%s: %s'%(self.project_status.name, self.sentence)

#@serializer()
class Step(models.Model):
    """
    Etapes
    """
    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")
        ordering = ['name']
    
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
        ordering = ['zipcode']
        
    zipcode = models.CharField(max_length=32, verbose_name=_('zip code'))
    name = models.CharField(max_length=256, verbose_name=_('Name'))
    
    objects = models.GeoManager()
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True, default=None)
    
    def natural_key(self):
        return (self.id, self.zipcode, self.name)
        
    def __unicode__(self):
        return '%s %s'%(self.zipcode, self.name)

@serializer(exclude=('description',))
class ProjectWorth(models.Model):
    """
    Capital gain?
    """
    class Meta:
        verbose_name = _("Project worth")
        verbose_name_plural = _("Project worth")
        ordering = ['name']
        
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    
    def natural_key(self):
        return (self.id, self.name)
    def __unicode__(self):
        return self.name
        
        
@serializer()
class BudgetRange(models.Model):
    class Meta:
        verbose_name = _("Budget range")
        verbose_name_plural = _("Budget ranges")
        ordering = ['floor']
        
    floor = models.IntegerField(verbose_name=_('Floor'))
    ceiling = models.IntegerField(verbose_name=_('Ceiling'))
    
    def __unicode__(self):
        if self.floor > 0 and self.ceiling > 0:
            return u'%s € - %s €'%(localize(self.floor), localize(self.ceiling))
        elif self.floor > 0:
            return u'> %s €'%(localize(self.floor), )
        else:
            return u'< %s €'%(localize(self.ceiling), )
    
@serializer()
class SurfaceRange(models.Model):
    class Meta:
        verbose_name = _("Surface range")
        verbose_name_plural = _("Surface ranges")
        ordering = ['floor']
        
    floor = models.IntegerField(verbose_name=_('Floor'))
    ceiling = models.IntegerField(verbose_name=_('Ceiling'))
    
    def __unicode__(self):
        if self.floor > 0 and self.ceiling > 0:
            return u'%s m² - %s m²'%(localize(self.floor), localize(self.ceiling))
        elif self.floor > 0:
            return u'> %s m²'%(localize(self.floor), )
        else:
            return u'< %s m²'%(localize(self.ceiling), )
        
        
@serializer(property_list = (
                            'centroid', 
                            'geojson', 
                            'partnerships', 
                            'image',
                            'city',
                            'surface_range',
                            'budget_range',
                            'procedure',
                            'mission',
                            'trade_object',
                            'programs',
                            'image',
                            'functions',
                            'actions', 
                            'worth',
                            ), 
            exclude=('mpoly','parent', 'published','activity_start', 'activity_end', 'steps'),
            filter=({'published':True},),
            depth=0)
class Project(models.Model):
    """
    A project is the main item to present on the website,
    everything else is more or less related to a project
    """
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['name']
    
    published = models.BooleanField(verbose_name=_('Published'),default=False)
    name = models.CharField(verbose_name=_('Name'),max_length=1024)
    description = models.TextField(verbose_name=_('Description'),blank=True, null=True, default=None)
    address = models.TextField(verbose_name=_('Address'),blank=True, null=True, default=None)
    trade_name = models.TextField(verbose_name=_('Trade name'), blank=True, default='')
    attribution = models.IntegerField(verbose_name=_('Attribution'),max_length=512, blank=True, null=True)
    
    activity_start = models.DateField(verbose_name=_('Activity start'), blank=True, null=True, default=None)
    activity_end = models.DateField(verbose_name=_('Activity end'), blank=True, null=True, default=None)
    
    city = models.ForeignKey('City', verbose_name=_('City'),blank=True, null=True, default=None)
    surface_range = models.ForeignKey('SurfaceRange', verbose_name=_('Surface'),blank=True, null=True, default=None)
    budget_range = models.ForeignKey('BudgetRange', verbose_name=_('Budget'), blank=True, null=True, default=None)
    procedure = models.ForeignKey('Procedure', verbose_name=_('Procedure'),blank=True, null=True, default=None)
    mission = models.ForeignKey('Mission', verbose_name=_('Mission'),blank=True, null=True, default=None)
    
    trade_object = models.ManyToManyField('TradeObject', verbose_name=_('Trade object'),blank=True, null=True, default=None)
    programs = models.ManyToManyField('Program', verbose_name=_('Programs'),blank=True, null=True, default=None)
    image = models.ManyToManyField('ProjectImage', verbose_name=_('Project Images'),blank=True, null=True, default=None)
    functions = models.ManyToManyField('Function', verbose_name=_('Functions'),blank=True, null=True, default=None)
    steps = models.ManyToManyField('Step', blank=True)
    actions = models.ManyToManyField('Action', verbose_name=_('Actions'),blank=True, null=True, default=None)
    worth = models.ManyToManyField('ProjectWorth', verbose_name=_('Project worths'),blank=True, null=True, default=None)
    
    
    mpoly = models.MultiPolygonField(verbose_name=_('Perimeter'), srid=4326, geography=True, blank=True, null=True, default=None)
    objects = models.GeoManager()
    
    parent = models.ForeignKey( 'Project', verbose_name=_('Parent'), blank=True, null=True, default=None)
    
    slug = models.SlugField(max_length=255, editable=False, default='None')
    
    def get_city_display(self):
        try:
            return '%s %s'%(self.city.zipcode, self.city.name)
        except Exception:
            return ''
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(force_insert, force_update) 
    
    @property
    def centroid(self):
        try:
            return json.loads(self.mpoly.centroid.geojson)
        except Exception:
            return  { "type": "Point", "coordinates": [ 0, 0 ] }
        
    @property
    def geojson(self):
        try:
            return json.loads(self.mpoly.geojson)
        except Exception:
            return  None
    
        
    def __unicode__(self):
        return self.name







