from django.conf.urls import patterns, include, url

urlpatterns = patterns('bmabru.views',
    url(r'^$', 'index', name='index'),
    url(r'^project/(?P<project>.+)$', 'project', name='project'),
    url(r'^projects/$', 'projects', name='projects'),
    url(r'^projects/json/$', 'projects_json'),
    url(r'^structure$', 'expose_structure'),
    url(r'^bind_geometry', 'bind_geometry'),
)