from django.conf.urls import patterns, include, url

#from python4unite.views import index
from heyi.views import index, product_cate, contactus, show_pages

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

    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^products/$', product_cate),
    url(r'^contactus/$', contactus),
    url(r'^pages/(.+)/$', show_pages)
)
