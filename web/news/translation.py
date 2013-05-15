"""
news.translation
"""

from modeltranslation.translator import translator, TranslationOptions
from news.models import *

class ItemTrOptions(TranslationOptions):
    fields = ('title', 'body')
    
translator.register(Item, ItemTrOptions)
