"""
admin custom
"""

from django.contrib import admin
from django.contrib.gis import admin as geo_admin
from django.forms import ModelForm
from bmabru.models import *


admin.site.register(PartnerType)
admin.site.register(Partner)
admin.site.register(Builder)
admin.site.register(Program)
admin.site.register(Procedure)
admin.site.register(ProjectImage)
admin.site.register(Project, geo_admin.GeoModelAdmin)

