from django.conf.urls import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^$', 'index', name='index'),
    url(r'^parser$', 'parser', name='parser'),
)