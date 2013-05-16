"""
media.models
"""

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable

from bmabru.models import Project

from bma.api import serializer


class Resource(models.Model):
    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        
    name = models.CharField(max_length=256)
    path = models.FileField(upload_to='resources/%Y/%m/%d')
    
    def __unicode__(self):
        return self.name

class Category(Sortable):
    class Meta(Sortable.Meta):
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        
    name = models.CharField(max_length=128)
    
    def pages(self):
        return self.page_set.filter(published=True)
    
    def __unicode__(self):
        return self.name
        
class Featured(Sortable):
    class Meta(Sortable.Meta):
        verbose_name = _("Featured")
        verbose_name_plural = _("Featured")
    
    ftype = models.CharField(max_length=2, editable=False)
    published = models.BooleanField(default=False)
    page = models.ForeignKey('Page', blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    
    def pretty_display(self):
        if self.ftype == 'PA':
            return self.page.title
        return self.project.name
        
    def __unicode__(self):
        return self.pretty_display()
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.page:
            self.ftype = 'PA'
        if self.project:
            self.ftype = 'PR'
        super(Featured, self).save(force_insert, force_update)
        
class SubjectiveImage(Sortable):
    class Meta(Sortable.Meta):
        verbose_name = _("Subjective Image")
        verbose_name_plural = _("Subjective Images")
        
    image = models.ImageField(upload_to='media_subjective', height_field='image_height', width_field='image_width', blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True, default=0)
    image_height = models.IntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        words = self.note.split(' ')
        excerpt = ' '.join(words[0:8])
        return '[%s] %s'%(self.image, excerpt)
        
@serializer()
class Page(Sortable):
    class Meta(Sortable.Meta):
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        
    slug = models.SlugField(max_length=255, editable=False)
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=512)
    body = models.TextField()
    published = models.BooleanField(default=False)
    resources = models.ManyToManyField('Resource', blank=True, null=True)
    image = models.ImageField(upload_to='media_page', height_field='image_height', width_field='image_width', blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True, default=0)
    image_height = models.IntegerField(blank=True, null=True, default=0)
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(force_insert, force_update)