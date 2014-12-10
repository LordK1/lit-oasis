from django.conf.urls import patterns, url

__author__ = 'k1'

urlpatterns = patterns(
    'article.views',
    url(r'^get/(\d+)/$', 'detail', name='detail'),
    url(r'^category/(\d+)/$', 'category', name='category'),
    url(r'^vote/(?P<author_id>\d+)/$', 'vote', name='vote'),
)
