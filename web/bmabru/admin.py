"""
admin custom
"""

from django.contrib import admin
from django.contrib.gis import admin as geo_admin
from django.forms import ModelForm
from bmabru.models import *


class GeoAdmin(geo_admin.GeoModelAdmin):
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
        self.openlayers_url = 'http://bma.local/web_static/lib/OpenLayers-2.12/OpenLayers.js'
        self.map_width = 800
        self.map_height = 600

admin.site.register(PartnerType)
admin.site.register(Partner)
admin.site.register(Builder)
admin.site.register(Program)
admin.site.register(Procedure)
admin.site.register(ProjectImage)
#admin.site.register(Project, geo_admin.OSMGeoAdmin)
admin.site.register(Project, GeoAdmin)

