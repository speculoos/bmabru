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
    Organisations working with bMa
    """
    name = models.CharField(max_length=512)
    url = models.URLField(blank=True)
    ptype = models.ForeignKey('PartnerType', related_name='partners')
    
    
    def __unicode__(self):
        return '%s (%s)'%(self.name, self.ptype)
        
        
class Builder(models.Model):
    """
    Describe builders _(maitres d'ouvrage)
    """
    name = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.name
        
        
        
class Program(models.Model):
    """
    building programs
    """
    name = models.CharField(max_length=512)
    features = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.name


class Procedure(models.Model):
    """
    Procédure
    """
    
    name = models.CharField(max_length=512)
    ptype = models.CharField(max_length=512)
        
        
        
class ProjectImage(models.Model):
    """
    An illustration for a project
    """
    image = models.ImageField(upload_to='project_trigo', height_field='height', width_field='width')
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    zoom_level = models.IntegerField(blank=True)

class Project(models.Model):
    """
    A project is the main item to present on the website,
    everything else is more or less related to a project
    """
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    contrib = models.TextField(blank=True)
    
    builders = models.ManyToManyField('Builder')
    program = models.ForeignKey('Program')
    procedure = models.ForeignKey('Procedure')
    image = models.ForeignKey('ProjectImage')
    
    mpoly = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name







