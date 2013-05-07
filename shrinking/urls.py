from django.conf.urls import patterns, include, url

import portfolio

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio.views.index', name='portfolio'),
    # url(r'^shrinking/', include('shrinking.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
