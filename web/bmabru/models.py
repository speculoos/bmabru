# -*- coding: utf-8 -*-
"""

"""

from django.contrib.gis.db import models




class PartnerType(models.Model):
    """
    Define custom partner types
    """
    name = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.name
    
    
class Partner(models.Model):
    """
    Organisations connected to bMa
    """
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
        
        

class Program(models.Model):
    """
    building programs
    """
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name


class Procedure(models.Model):
    """
    Procédure
    """
    
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
        
        
class ProjectImage(models.Model):
    """
    An illustration for a project
    """
    image = models.ImageField(upload_to='project_trigo', height_field='height', width_field='width')
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    zoom_level = models.IntegerField(blank=True)
    
    
class Function(models.Model):
    """
    Fonction du projet
    """
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

        
class Mission(models.Model):
    """
    Type de mission
    """
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
        
        

        
class ProjectStatus(models.Model):
    """
    Etat d'avancement du projet
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    order = models.IntegerField()
    
    def __unicode__(self):
        return self.name
        
class Action(models.Model):
    """
    ???
    """
    sentence = models.TextField()
    project_status = models.ForeignKey('ProjectStatus')
    
    def __unicode__(self):
        return '%s / %s'%(self.project_status.name, self.sentence[:32])


class Step(models.Model):
    """
    Etapes
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
        
class City(models.Model):
    zipcode = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
    
class Project(models.Model):
    """
    A project is the main item to present on the website,
    everything else is more or less related to a project
    """
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
    
    @property
    def centroid(self):
        return self.mpoly.centroid.geojson
        
    @property
    def geojson(self):
        return self.mpoly.geojson
    
        
    def __unicode__(self):
        return self.name







