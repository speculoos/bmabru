"""
media.models
"""

from django.db import models
from django.template.defaultfilters import slugify





class Resource(models.Model):
    name = models.CharField(max_length=256)
    path = models.FileField(upload_to='resources/%Y/%m/%d')
    
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
        
class Page(models.Model):
    slug = models.SlugField(max_length=255, editable=False)
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=512)
    body = models.TextField()
    published = models.BooleanField(default=False)
    resources = models.ManyToManyField('Resource', blank=True)
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(force_insert, force_update)