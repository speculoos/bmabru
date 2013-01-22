"""
media.translation
"""

from modeltranslation.translator import translator, TranslationOptions
from media.models import *

class CategoryTypeTrOptions(TranslationOptions):
    fields = ('name',)
    
class PageTrOptions(TranslationOptions):
    fields = ('title', 'body')


translator.register(Category, CategoryTypeTrOptions)
translator.register(Page, PageTrOptions)
