"""
bmabru.translation
"""

from modeltranslation.translator import translator, TranslationOptions
from bmabru.models import *

class PartnerTypeTrOptions(TranslationOptions):
    fields = ('name',)
    
class PartnerTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class PartnershipTypeOptions(TranslationOptions):
    fields = ('name', 'description')
    
class TradeObjectOptions(TranslationOptions):
    fields = ('name', 'description')
    
class ProjectWorthOptions(TranslationOptions):
    fields = ('name', 'description')
    
class ProgramTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class ProcedureTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class FunctionTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class MissionTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class ProjectStatusTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class ActionTrOptions(TranslationOptions):
    fields = ('sentence', )
    
class StepTrOptions(TranslationOptions):
    fields = ('name', 'description')
    
class CityTrOptions(TranslationOptions):
    fields = ('name',)
    
class ProjectTrOptions(TranslationOptions):
    fields = ('name', 'description', 'address')

translator.register(PartnerType, PartnerTypeTrOptions)
translator.register(Partner, PartnerTrOptions)
translator.register(PartnershipType, PartnershipTypeOptions)
translator.register(TradeObject, TradeObjectOptions)
translator.register(ProjectWorth, ProjectWorthOptions)
translator.register(Program, ProgramTrOptions)
translator.register(Procedure, ProcedureTrOptions)
translator.register(Function, FunctionTrOptions)
translator.register(Mission, MissionTrOptions)
translator.register(ProjectStatus, ProjectStatusTrOptions)
translator.register(Action, ActionTrOptions)
translator.register(Step, StepTrOptions)
translator.register(City, CityTrOptions)
translator.register(Project, ProjectTrOptions)
