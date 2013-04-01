# -*- coding: utf-8 -*-
"""

"""

from django.contrib.gis.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from bma.api import serializer


class PartnerType(models.Model):
    """
    Define custom partner types
    """
    class Meta:
        verbose_name = _("Partner type")
        verbose_name_plural = _("Partner types")
        
    name = models.CharField(max_length=512)
    
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
        
    name = models.CharField(max_length=512)
    url = models.URLField(blank=True)
    ptype = models.ForeignKey('PartnerType', related_name='partners')
    description = models.TextField(blank=True)
    contact_name = models.CharField(max_length=128, blank=True)
    subscribed = models.BooleanField(default=False)
    email = models.EmailField(max_length=128, blank=True)
    
    def natural_key(self):
        return (self.id, self.name)
    
    def __unicode__(self):
        return '%s (%s)'%(self.name, self.ptype)
        
        
@serializer()
class Program(models.Model):
    """
    building programs
    """
    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")
        
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
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
    
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
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
        
    image = models.ImageField(upload_to='project_trigo', height_field='height', width_field='width')
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
        
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
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
        
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
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
        
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
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
        
    sentence = models.TextField()
    project_status = models.ForeignKey('ProjectStatus')
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
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
     
@serializer()
class City(models.Model):
    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        
    zipcode = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    def natural_key(self):
        return (self.id, self.zipcode, self.name)
    def __unicode__(self):
        return self.name
    
    
@serializer()
class Project(models.Model):
    """
    A project is the main item to present on the website,
    everything else is more or less related to a project
    """
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
    
    published = models.BooleanField(default=False)
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    surface = models.CommaSeparatedIntegerField(max_length=64,blank=True)
    budget = models.CommaSeparatedIntegerField(max_length=64,blank=True)
    
    city = models.ForeignKey('City', blank=True)
    partners = models.ManyToManyField('Partner')
    programs = models.ManyToManyField('Program')
    procedure = models.ForeignKey('Procedure')
    functions = models.ManyToManyField('Function')
    image = models.ManyToManyField('ProjectImage', blank=True)
    mission = models.ForeignKey('Mission', blank=True)
    
    steps = models.ManyToManyField('Step')
    actions = models.ManyToManyField('Action')
    
    
    mpoly = models.MultiPolygonField(srid=4326, geography=True)
    objects = models.GeoManager()
    
    slug = models.SlugField(max_length=255, editable=False, default='None')
    
    def get_city_display(self):
        return '%s %s'%(self.city.zipcode, self.city.name)
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(force_insert, force_update) 
    
    @property
    def centroid(self):
        try:
            return self.mpoly.centroid.geojson
        except:
            return  u'{ "type": "Point", "coordinates": [ 0, 0 ] }'
        
    @property
    def geojson(self):
        return self.mpoly.geojson
    
        
    def __unicode__(self):
        return self.name







