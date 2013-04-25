"""
news.models
"""

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class News(models.Model):
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        
    slug = models.SlugField(max_length=255, editable=False)
    title = models.CharField(max_length=512, verbose_name=_('Title'))
    body = models.TextField(verbose_name=_('Body'))
    pub_date = models.DateField(auto_now_add=True)
    
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(force_insert, force_update)