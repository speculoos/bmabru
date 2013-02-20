"""
admin custom
"""

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

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
    pass

admin.site.register(Resource)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

