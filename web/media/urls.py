from django.conf.urls import patterns, include, url

urlpatterns = patterns('media.views',
    url(r'json/(?P<mid>\d+)$', 'media_json'),
)
