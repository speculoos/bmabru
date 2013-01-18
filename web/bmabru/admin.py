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
        self.default_lon = 486139.499893721
        self.default_lat = 6593152.311766164
        self.default_zoom = 12
        self.map_srid = 900913
        self.units = 'm'
        self.num_zoom = 20

admin.site.register(PartnerType)
admin.site.register(Partner)
admin.site.register(Builder)
admin.site.register(Program)
admin.site.register(Procedure)
admin.site.register(ProjectImage)
admin.site.register(Project, geo_admin.OSMGeoAdmin)

