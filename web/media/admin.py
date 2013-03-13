"""
admin custom
"""

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _

from media.models import *


class TabbedTr:
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


    
class CategoryAdmin(TabbedTr, TranslationAdmin):
    pass

    
class PageAdmin(TabbedTr, TranslationAdmin):
    list_display = ('title', 'category', 'published')
    list_filter = ['category', 'published']
    search_fields = ['title', 'body']
    fieldsets = [
            (None, {'fields':(('published', 'category'),)}),
            (_('Content'), {'fields':('title', 'body')}),
            (_('Extra'), {'fields':('image', 'resources')})
            ]

admin.site.register(Resource)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

