from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog.ctlg.views import *


urlpatterns = patterns('catalog.ctlg.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', search),
    url(r'^(?P<cat>((?:[\w-]+/){1,3}))prod/(?P<unit>[\w-]+)/$', units),
    url(r'^(?P<cat>((?:[\w-]+/){1,3}))$', my_cat),
    url(r'^$', base),

)
