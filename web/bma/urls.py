from django.conf.urls import patterns, include, url
from django.conf import settings

import bma.api as api

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
    url(r'^news/', include('news.urls')),
    url(r'^i18n/$', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^templatejs/', include('templatejs.urls')),
    url(r'^api/$', 'bma.api.api_root', name='api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('bmabru.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^translate/', include('rosetta.urls')),
    )

urlpatterns += api.urls(
    (
        ('bmabru', 'Project', ({'published':True},)),
        ('media', 'Page', ({'published':True},)),
        ('news', 'Item', None),
        ('news', 'Resource', None),
    )
) 

