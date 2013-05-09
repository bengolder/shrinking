from django.conf.urls import patterns, include, url

import portfolio

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio.views.index', name='home'),
    url(r'^work/$', 'portfolio.views.work', name='work'),
    url(r'^work/(?<project_slug>[\w\-]+)/$', 'portfolio.views.project',
        name='project'),
    url(r'^people/$', 'portfolio.views.people', name='people'),
    # url(r'^shrinking/', include('shrinking.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
