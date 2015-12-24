from django.conf.urls import patterns, include, url

#from python4unite.views import index
from home.views import index

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python4unite.views.home', name='home'),
    # url(r'^python4unite/', include('python4unite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #64326073

    url(r'^$', index),
    url(r'^index/$', index)
)
