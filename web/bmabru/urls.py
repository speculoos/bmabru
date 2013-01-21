from django.conf.urls import patterns, include, url

urlpatterns = patterns('bmabru.views',
    url(r'^$', 'index'),
    url(r'^projects/$', 'projects_json'),
)
