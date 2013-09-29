from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from home.views import index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    # url(r'^optimal/', include('optimal.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
