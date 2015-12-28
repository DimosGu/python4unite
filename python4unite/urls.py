from django.conf.urls import patterns, include, url

#from python4unite.views import index
from heyi.views import index, products, about, realview, wenhua, honour, contactus, you_are_wanted

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
    url(r'^index/$', index),
    url(r'^products/$', products),
    url(r'^about/$', about),
    url(r'^realview/$', realview),
    url(r'^wenhua/$', wenhua),
    url(r'^honour/$', honour),
    url(r'^contactus/$', contactus),
    url(r'^you-are-wanted/$', you_are_wanted)
)
