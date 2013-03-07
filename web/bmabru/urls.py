from django.conf.urls import patterns, include, url

urlpatterns = patterns('bmabru.views',
    url(r'^$', 'index'),
    url(r'^project/(?P<project>.+)$', 'project'),
    url(r'^projects/$', 'projects'),
    url(r'^projects/json/$', 'projects_json'),
)
