from django.conf.urls import patterns, include, url
from news.views import IndexView

urlpatterns = patterns('news.views',
    url(r'^$', IndexView.as_view(), name='news_index'),
    url(r'^parser$', 'parser', name='parser'),
)

