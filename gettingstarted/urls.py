from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

import hello.views

urlpatterns = patterns('',
                       url(r'^$', hello.views.index, name='index'),
                       url(r'^article/', include('article.urls')),
                       url(r'^db', hello.views.db, name='db'),
                       url(r'^admin/', include(admin.site.urls)), )
