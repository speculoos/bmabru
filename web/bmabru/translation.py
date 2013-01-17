"""
bmabru.translation
"""

from modeltranslation.translator import translator, TranslationOptions
from bmabru.models import (PartnerType,)

class PartnerTypeTrOptions(TranslationOptions):
    fields = ('name',)
    
class ProjectTrOptions(TranslationOptions):
    fields = ('description', 'contrib', )

translator.register(PartnerType, PartnerTypeTrOptions)
