from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog.ctlg.views import *


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', search),
    url(r'^(?P<cat1>[\w-]+)/(?P<cat2>[\w-]+)/(?P<cat3>[\w-]+)/prod/(?P<unit>[\w-]+)/$', units3),
    url(r'^(?P<cat1>[\w-]+)/(?P<cat2>[\w-]+)/prod/(?P<unit>[\w-]+)/$', units2),
    url(r'^(?P<cat1>[\w-]+)/prod/(?P<unit>[\w-]+)/$', units1),
    url(r'^(?P<cat1>[\w-]+)/(?P<cat2>[\w-]+)/(?P<cat3>[\w-]+)/$', my_cat3),
    url(r'^(?P<cat1>[\w-]+)/(?P<cat2>[\w-]+)/$', my_cat2),
    url(r'^(?P<cat1>[\w-]+)/$', my_cat1),
    url(r'^$', base),

)
