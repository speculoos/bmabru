from django.conf.urls import patterns, include, url

urlpatterns = patterns('media.views',
    url(r'json/subjective_images/$', 'subjective_images_json'),
    url(r'json/(?P<mid>\d+)$', 'media_json'),
    url(r'^page/(?P<page_slug>.+)$', 'page', name='page'),
)
