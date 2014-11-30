from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'article.views.home', name='home'),
                       url(r'^article/', include('article.urls')),
                       url(r'^contact/', 'article.views.contact', name='contact'),
                       url(r'^admin/', include(admin.site.urls)), )
