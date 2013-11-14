"""
media.models
"""

from django.db import models
from django.core.mail import mail_managers
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable

from markdown2 import markdown
from textwrap import wrap
from easy_thumbnails.files import get_thumbnailer

from bmabru.models import Project

from bma.api import serializer

@serializer()
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
        

@serializer(property_list=('thumbnail','url', 'large'))
class SubjectiveImage(Sortable):
    class Meta(Sortable.Meta):
        verbose_name = _("Subjective Image")
        verbose_name_plural = _("Subjective Images")
        
    image = models.ImageField(upload_to='media_subjective', height_field='image_height', width_field='image_width', blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True, default=0)
    image_height = models.IntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True)
    
        
    @property
    def thumbnail(self):
        from easy_thumbnails.files import get_thumbnailer
        options = {'size': (360 /2, 240 /2), 'crop': True}
        return get_thumbnailer(self.image).get_thumbnail(options).url
        
    @property
    def large(self):
        from easy_thumbnails.files import get_thumbnailer
        options = {'size': (360 *3, 240 *3), 'crop': 'smart'}
        return get_thumbnailer(self.image).get_thumbnail(options).url
        
    @property
    def url(self):
        return self.image.url
    
    def __unicode__(self):
        words = self.note.split(' ')
        excerpt = ' '.join(words[0:8])
        return '[%s] %s'%(self.image, excerpt)
        
        
        
@serializer(property_list=('resources','format_body',))
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
    
    @property
    def format_body(self):
        return markdown(self.body)
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        cat = '~'
        if self.category:
            cat = self.category.name
        self.slug = slugify('-'.join([cat,self.title]))
        super(Page, self).save(force_insert, force_update)
        
        
        
@serializer(write_only=('name','email','message'), 
            perms=('AllowAny',))
class Message(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=128)
    message = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    def body(self):
        ret = []
        ret.append(u'%s <%s> %s:\n' % (self.name, self.email,_('sent')))
        for line in wrap(self.message):
            ret.append(line)
            
        return u'\n'.join(ret)
        
    

def message_sent(sender, **kwargs):
    message = kwargs['instance']
    print message.name
    print message.email
    
    body = message.body()
    mail_managers(_('New Message'), body)
    
    
models.signals.post_save.connect(message_sent, sender=Message, weak=False)
    
        