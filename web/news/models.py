"""
news.models
"""

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from bmabru.models import Project
from bma.api import serializer

class Resource(models.Model):
    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        
    
@serializer()
class Item(models.Model):
    class Meta:
        verbose_name = _("News Item")
        verbose_name_plural = _("News Items")
        ordering = ['pub_date']
        
    slug = models.SlugField(max_length=255, editable=False)
    title = models.CharField(max_length=512, verbose_name=_('Title'))
    body = models.TextField(verbose_name=_('Body'))
    pub_date = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name='+', blank=True, null=True, default=None)
    resource = models.ForeignKey(Resource, blank=True, null=True, default=None)
    
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Item, self).save(force_insert, force_update)
        
