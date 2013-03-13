"""
media.models
"""

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _





class Resource(models.Model):
    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        
    name = models.CharField(max_length=256)
    path = models.FileField(upload_to='resources/%Y/%m/%d')
    
    def __unicode__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
        
class Page(models.Model):
    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        
    slug = models.SlugField(max_length=255, editable=False)
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=512)
    body = models.TextField()
    published = models.BooleanField(default=False)
    resources = models.ManyToManyField('Resource', blank=True)
    image = models.ImageField(upload_to='media_page', height_field='image_height', width_field='image_width', blank=True)
    image_width = models.IntegerField(blank=True, default=0)
    image_height = models.IntegerField(blank=True, default=0)
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(force_insert, force_update)