from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'article.views.home', name='home'),
                       url(r'^article/', include('article.urls'), name='articles'),
                       url(r'^contact/', 'article.views.contact', name='contact'),
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
