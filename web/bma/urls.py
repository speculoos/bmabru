from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

##js_info_dict = {
    ##'domain': 'djangojs',
    ##'packages': ('web',),
##}

urlpatterns = patterns('',
    url(r'^config/(?P<q>.+)$', 'bma.views.config'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/', include('media.urls')),
    url(r'^i18n/$', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^', include('bmabru.urls')),
)
