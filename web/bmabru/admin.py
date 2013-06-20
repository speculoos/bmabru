"""
admin custom
"""

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.forms import ModelForm
from django.contrib.gis import admin as geo_admin

from modeltranslation.admin import TranslationAdmin

from django.utils.translation import ugettext_lazy as _

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
    search_fields = ['name',]
    
class PartnerAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    list_display = ('name', 'ptype')
    list_filter = ('ptype',)
    
class PartnershipTypeAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class ProgramAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class ProcedureAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class FunctionAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class MissionAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class ProjectStatusAdmin(TabbedTr, TranslationAdmin):
    pass
    
class ActionAdmin(TabbedTr, TranslationAdmin):
    pass
    
class StepAdmin(TabbedTr, TranslationAdmin):
    pass
    
class CityAdmin(TabbedTr, TranslationAdmin):
    pass
    
class TradeObjectAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class ProjectWorthAdmin(TabbedTr, TranslationAdmin):
    search_fields = ['name',]
    
class PartnershipInline(admin.TabularInline):
    model = Partnership
    extra = 1
    fieldset_id = 'partnership_set'
    after_field = 'budget_range'

class ProjectCityListFilter(SimpleListFilter):
    title = _('City')
    parameter_name = 'city_id'
    
    def lookups(self, request, model_admin):
        ret = []
        cities = City.objects.all()
        for c in cities:
            ret.append((c.id, '%s %s'%(c.zipcode, c.name)))
        return ret
        
    def queryset(self, request, queryset):
        if self.parameter_name in request.GET:
            return queryset.filter(city__id=self.value())
        return queryset
        
class ProjectForm(ModelForm):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'geo_tabbed_translation_fields.js',
            'admin_override/SelectBox.js'
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        choices = []
        for project_status in ProjectStatus.objects.all():
            #choices.append([project_status.name,  project_status.action_set.all()])
            action_choice = []
            for action in project_status.action_set.all():
                action_choice.append([action.id, action.sentence])
            choices.append([project_status.name, action_choice])
            
                
        self.fields['actions'].choices = choices


class GeoAdmin(geo_admin.GeoModelAdmin, TranslationAdmin):
    
    filter_horizontal = ('programs', 'functions', 'image',  'worth', 'actions', 'trade_object')
    fieldsets = [
            (None, {'fields':('published',)}),
            (_('Description'),{
                'fields': (
                    'name', 
                    'description', 
                    ('address', 'city'),
                    'functions',
                    'surface_range', 
                    'budget_range',
                    'programs',
                    'trade_name'
                    )
            }),
            (_('bMa'),{
                'fields': (
                    'trade_object',
                    'procedure',
                    'mission',
                    'actions',
                    'worth',
                    ('activity_start', 'activity_end')
                    )
            }),
            (_('Project'),{
                'fields':(
                    'attribution',
                    'mpoly',
                    'image'
                    )
            }),
            (None, {'fields':('parent',)}),
        ]
    form = ProjectForm
    list_display = ('name', 'address', 'get_city_display', 'published')
    list_filter = (ProjectCityListFilter, 'published')
    search_fields = ['name',]
    inlines = [PartnershipInline]
    
    def __init__(self, model, admin_site):
        super(GeoAdmin, self).__init__(model, admin_site)
        #self.wms_url = 'http://bmawms.specgis.be/service'
        self.wms_url = 'http://geoserver.gis.irisnet.be/geoserver/wms'
        self.wms_layer = 'urbisFR'
        self.wms_name = 'urbisFR'
        self.wms_options = {'format': 'image/png'}
        self.default_lon = 498980.9206456305 # 4.360312
        self.default_lat = 6584591.364598221 # 50.844894
        self.default_zoom = 12
        #self.map_srid = 900913
        self.map_srid = 31370
        self.units = 'm'
        self.num_zoom = 20
        self.openlayers_url = '/'.join([settings.STATIC_URL, 'lib/OpenLayers-2.12/OpenLayers.js'])
        self.map_width = 800
        self.map_height = 600
        

admin.site.register(PartnershipType, PartnershipTypeAdmin)
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
admin.site.register(ProjectWorth, ProjectWorthAdmin)
admin.site.register(SurfaceRange)
admin.site.register(BudgetRange)
admin.site.register(TradeObject, TradeObjectAdmin)
admin.site.register(Project, GeoAdmin)

