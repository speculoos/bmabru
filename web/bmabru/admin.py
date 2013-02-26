"""
admin custom
"""

from django.contrib import admin
from django.contrib.gis import admin as geo_admin

from modeltranslation.admin import TranslationAdmin

from bmabru.models import *
import bma.settings as settings


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

class PartnerTypeAdmin(TabbedTr, TranslationAdmin):
    pass
    
class PartnerAdmin(TabbedTr, TranslationAdmin):
    pass
    
class ProgramAdmin(TabbedTr, TranslationAdmin):
    pass
    
class ProcedureAdmin(TabbedTr, TranslationAdmin):
    pass
    
class FunctionAdmin(TabbedTr, TranslationAdmin):
    pass
    
class MissionAdmin(TabbedTr, TranslationAdmin):
    pass
    
class ProjectStatusAdmin(TabbedTr, TranslationAdmin):
    pass
    
class ActionAdmin(TabbedTr, TranslationAdmin):
    pass
    
class StepAdmin(TabbedTr, TranslationAdmin):
    pass
    
class CityAdmin(TabbedTr, TranslationAdmin):
    pass


class GeoAdmin(geo_admin.GeoModelAdmin, TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'geo_tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    filter_horizontal = ('partners', 'programs', 'functions', 'image', 'actions', 'steps')
    def __init__(self, model, admin_site):
        super(GeoAdmin, self).__init__(model, admin_site)
        self.wms_url = 'http://bmawms.specgis.be/service'
        self.wms_layer = 'bMa'
        self.wms_name = 'bMa'
        self.wms_options = {'format': 'image/png'}
        self.default_lon = 498980.9206456305 # 4.360312
        self.default_lat = 6584591.364598221 # 50.844894
        self.default_zoom = 12
        self.map_srid = 900913
        self.units = 'm'
        self.num_zoom = 20
        self.openlayers_url = '/'.join([settings.STATIC_URL, 'lib/OpenLayers-2.12/OpenLayers.js'])
        self.map_width = 800
        self.map_height = 600
        

admin.site.register(PartnerType, PartnerTypeAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Function, FunctionAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ProjectImage)
admin.site.register(Project, GeoAdmin)

