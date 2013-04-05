from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('bmabru.views',
    url(r'^$', 'index', name='index'),
    url(r'^structure$', 'expose_structure'),
)

